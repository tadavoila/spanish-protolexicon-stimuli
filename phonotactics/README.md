# Spanish proto-lexicon

## Phonotactic probability scripts
*Copied from supplementary materials of Oh et al. (2020)*

### Contents

This directory contains scripts used to calculate phonotactic probabilities, used in the analysis.

Scripts should be run in a POSIX shell and require [SRILM](https://www.sri.com/platform/srilm/) and Python.

- `modify-lm_parsed.py`: a script for modifying a language model trained on morphs for the assumption that participants attempt to parse stimuli into morphs  
- `morph-boundary.txt`: the character used to represent morph boundaries (+)  
- `reformat-srilm-evaluation.py`: a script for extracting phonotactic probabilities from a .DEBUG file output by SRILM  
- `score-parsed.sh`: a script for evaluating morph-based phonotactic probabilities of stimuli, assuming that participants attempt to parse stimuli into morphs, where the training data are types that should all be weighted equally  
- `score-unparsed.sh`: a script for evaluating word-based phonotactic probabilities of stimuli, or morph-based phonotactic probabilities assuming that participants do not parse stimuli into morphs, where the training data are types that should all be weighted equally  
- `stimuli.txt`: the stimuli for Exp2, in a format for processing by SRILM (phonological form, with phonemes separated by spaces). Used for `score-unparsed` scripts.  
- `stimuli_parsed.txt`: the stimuli for Exp2, with start/end morph boundaries added, in a format for processing by SRILM (phonological form, with phonemes separated by spaces). Used for `score-parsed` scripts.  
- `train/`: a directory containing files used to train phonotactic models.  

### Using the scripts

The following are arguments for all of the shell scripts:  
1. `<TRAIN>`: the path to the data that will be used to train the phonotactic model  
  - The training data should be a plaintext file with a single column, no headings. Each row should contain a single word/morph, with a space between each phoneme character.  
2. `<STIMLIST>`: the path to the stimuli that will be scored  
  - Should be one of `stimuli.txt` or `stimuli_parsed.txt`, depending on the type of model being trained  
3. `<LMDIR>`: the path to a directory where the language model files will be stored.  
  - Note there should be no trailing `/`  
4. `<AUXDIR>`: the path to the directory where debug files from scoring stimuli will be stored.  
  - Note there should be no trailing `/`  
5. `<OUTDIR>`: the path to the directory where the scored stimuli files will be stored.  
  - Note there should be no trailing `/`  

For example, to score the stimuli according to a morph-based phonotactic model that assumes participants attempt to parse stimuli into morphs, use the following code (assuming the directories `phonotactic-models`, `stimuli-scores`, and `stimuli-scores/auxiliaries` have been created):  
  >`sh score-parsed.sh train/morphs.txt stimuli_parsed.txt phonotactic-models stimuli-scores/auxiliaries stimuli-scores`  