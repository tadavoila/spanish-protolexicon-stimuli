import json
import re
import argparse

def load_rules(rules_path):
    """Loads a list of rewrite rules from JSON form, where each
    rule is a triple of strings (target, environment, replacement),
    and reformats it to a list of rules where the target and
    environment are combined in a pre-compiled regular expression.
    """
    with open(rules_path, encoding="utf=8") as in_file:
        rules = json.load(in_file)
    reformatted_rules = [reformat_rule(rule) for rule in rules]
    return reformatted_rules

def reformat_rule(rule):
    """Reformats a rule from a triple of strings of format
    (target, environment, replacement)
    to a pair of format
    (target, regex, replacement)
    where regex is a pre-compiled regex containing the
    merged target and environment pattern.
    When the rule applies regardless of environment, None is
    used as the regex (to allow use of faster string replacement)
    """
    (target, environment, replacement) = rule
    (left_env, right_env) = environment.split("_")
    if left_env:
        if right_env:
            regex = re.compile(r"(?<={}){}(?={})".format(left_env, target, right_env))
        else:
            regex = re.compile(r"(?<={}){}".format(left_env, target))
    elif right_env:
        regex = re.compile(r"{}(?={})".format(target, right_env))
    else:
        regex = None
    return (target, regex, replacement)

def process_word(word, rules):
    """Applies rewrite rules to a word, to convert it from
    orthographic to phonological form (or phonological to phonetic).
    
    Arguments
    ---------
    word: str; a word in orthographic form.
    rules: list(tuple(str, regex, str)); a list of rewrite rules.
    """
    processed_word = word
    for rule in rules:
        processed_word = apply_rule(rule, processed_word)

    return processed_word

def apply_rule(rule, word):
    """Applies a rewrite rule to a word.
    
    Arguments
    ---------
    rule: tuple(str; regex, str); a rewrite rule as a triple, where the
          first element is the target, the second element is a 
          pre-compiled regular expression matching the target in an 
          environment, and the third element is a string to replace 
          that target with in that environment.
          When the rule applies regardless of environment, None is
          used as the regex (to allow use of faster string replacement)
    word: str; a word to which the rewrite rule will be applied.
    """
    (target, pattern, replacement) = rule
    # Timesaver: only proceed if the word contains the target
    # (faster to do this than check the pattern matches!)
    if target in word:
        if pattern is None:
            processed_word = word.replace(target, replacement)
        else:
            processed_word = pattern.sub(replacement, word)
        return processed_word
    else:
        return word

def process_file(words_path, rules_path, output_path):
    """Process a file of words by applying a list of rewrite rules,
    saving the output to a new file.
    
    Arguments
    ---------
    words_path: str; the path to a file containing the words to
                process, one per line
    rules_path: str; the path to a JSON file containing the rewrite
                rules, each in the format [target, environment, replacement]
    output_path: str; the path to the output file to create
    """
    rules = load_rules(rules_path)
    with open(words_path, encoding="utf-8") as in_file:
        with open(output_path, "w", encoding="utf-8") as out_file:
            for line in in_file:
                word = line.strip()
                processed_word = process_word(word, rules)
                out_file.write(processed_word + "\n")

if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description= "Applies rewrite rules to words")
    parser.add_argument("words_path", type=str, help="Path to a file containing words to process, \
                        one per line")
    parser.add_argument("rules_path", type=str, help="Path to a JSON file containing rewrite rules")
    parser.add_argument("output_path", type=str, help="Path to the output file")
    args = parser.parse_args()
    
    process_file(args.words_path, args.rules_path, args.output_path)
