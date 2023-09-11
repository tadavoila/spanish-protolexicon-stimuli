# Spanish proto-lexicon

## Phonological conversion scripts

### Contents

This directory contains a script used to convert Spanish words from orthographic to phonological form, used in the analysis.

Scripts should be run in a POSIX shell and require [eSpeak NG](https://github.com/espeak-ng/espeak-ng) and Python.

- `post-conversion_rules.json`: a file that lists the rewrite rules used to tidy up after eSpeak NG has converted the word to phonological form. Each rule is formatted as a triple, where the first element is the target of the rewrite rule, the second element is the environment , and the third element is the replacement. Rules are applied in the order listed.  
- `rewrite_forms.py`: a script for converting from IPA (as output by eSpeak NG) to custom phonological format, using the rewrite rules provided in `post-conversion_rules.json`  
- `spanish-orth2phon.sh`: a script for converting a list of Spanish words from orthographic to phonological form, using eSpeak NG and custom tidy-up rewrite rules  

### Using the script

The following are arguments for the shell script `spanish-orth2phon.sh`:  
1. `<ORTHFILE>`: the path to the list of Spanish words in orthographic form  
  - There should be one word per line.  
2. `<PHONFILE>`: the path to the output file that will be created, where the words are converted to phonological form  
3. `<RULEJSON>`: the path to a JSON file of rewrite rules to be applied after eSpeak NG, to convert from IPA format and tidy up.  
  - If this argument is left out, `post-conversion_rules.json` will be used by default  

For example, to convert a list of words in a file `words_orth.txt`, use the following code:  
  >`sh spanish-orth2phon.sh words_orth.txt words_phon.txt`  