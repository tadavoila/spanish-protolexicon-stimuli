#!/bin/bash

# score-parsed.sh
#
# Score a stimulus set based on morph phonotactics, without frequency weighting, assuming that stimuli are to be parsed into morphs.
#
# SYNTAX: sh score-parsed.sh <TRAIN> <STIMLIST> <LMDIR> <AUXDIR> <OUTDIR>

TRAIN=$1
STIMLIST=$2
LMDIR=$3
AUXDIR=$4
OUTDIR=$5

TRAINFILE=$(basename -- "$TRAIN")
TRAINROOT="${TRAINFILE%.*}"
LM="${LMDIR}/${TRAINROOT}.lm"
DEBUG="${AUXDIR}/${TRAINROOT}.debug"

# echo
# echo "Estimating language model"

# first run SRILM to get a language model
ngram-count -text $TRAIN -lm $LM -order 3 -wbdiscount -interpolate

# modify the language model to use morpheme boundary symbols and rule out adjacent boundaries
python modify-lm_parsed.py $LM

# echo
# echo "Scoring stimuli"

# use the language model to score the stimlist, over all possible segmentations
ngram -lm $LM -ppl $STIMLIST -debug 2 -hidden-vocab morph-boundary.txt -no-eos -no-sos > $DEBUG

# reformat the output
python reformat-srilm-evaluation.py $DEBUG $OUTDIR $STIMLIST --parsed

# echo
# echo "Done"