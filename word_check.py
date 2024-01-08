#!/usr/bin/env python3

def word_check(word, usersinput, correct_rows, current_word):
    split_word = list(word.lower())
    if len(usersinput) > len(split_word) or len(usersinput) < len(split_word):
        return "error" 
    for letter in range(len(word)):
        if usersinput[letter] == split_word[letter]:
            correct_rows[current_word][letter] = "cr"
        elif usersinput[letter] in split_word:
            correct_rows[current_word][letter] = "wp"
    return correct_rows
    
    
if __name__ == ("__main__"):
    print("Don't run me, run main.py!")