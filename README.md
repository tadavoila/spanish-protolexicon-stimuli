# Stimuli redesign for Spanish proto-lexicon experiments
Conducted word-based and morph-based phonotactic scoring and analysis of 200000 fake Spanish words using Python Pandas, SRILM, and Morfessor to generate a set of stimuli for an experiment examining Spanish proto-lexicons

- ``final.ipynb``: Implementation to generate the stimuli
- ``final.csv``: Final data frame of stimuli from final.ipynb
- ``all_scores.csv``: Data frame bank of all stimuli from final.ipynb before sorting for top 3

Developed an SQL tool to query word frequency and score data from 1000 sample stimuli databases and determined best samples by calculating Jensen-Shannon divergence 1000 times for 30 classifications of data using kernel density curves

- ``js_scores.ipynb``: Implementation of an SQL tool to analyze/query the stimuli

Materials
- ``data``: English words, Spanish words, and Spanish non-words 
- ``morfessor``: Files for use in Morfessor application and resulting data
- ``orth2phon``: Files for converting words from orthographic form to phonotactic form and resulting data
- ``phonotactics``: Files for phonotactic scoring and resulting data
- [Wuggy](http://crr.ugent.be/programs-data/wuggy): Generates non-words from word list
- [SRILM](http://www.speech.sri.com/projects/srilm/download.html): Language modeling toolkit 
- [Morfessor](https://morfessor.readthedocs.io/en/latest/): Outputs word morphs
- [eSpeak Ng](https://github.com/espeak-ng/espeak-ng): Outputs phonological word forms
