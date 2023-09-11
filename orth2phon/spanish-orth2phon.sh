#!/bin/bash

# spanish-orth2phon.sh
#
# Convert a list of orthographic Spanish words into phonological form,
# with one ASCII character per phone, separated by spaces.
#
# SYNTAX: sh spanish-orth2phon.sh <ORTHFILE> <PHONFILE> [<RULEJSON>]
# where ORTHFILE is the input PHONFILE is the output, and RULEJSON is an
# optional alternative file to use for post-processing rewrite rules
# (defaults to post-conversion_rules.json).

ORTHFILE=$1
PHONFILE=$2
RULEJSON=${3:-'post-conversion_rules.json'}

IPAFILE="${PHONFILE%.*}_ipa.txt"

# Process file with espeak
cat $ORTHFILE | espeak-ng -qx -ves-419 --ipa --sep=" " --phonout $IPAFILE

# Perform post-conversion
python rewrite_forms.py $IPAFILE $RULEJSON $PHONFILE

# Remove IPA file
rm -f $IPAFILE