#-------------------------------------------------------------------------------|
#   Title:          AddingWhitespace                                            |
#   Author:         Drake G. Cummings                                           |
#   Purpose:        Add correct whitespace to a file                            |
#-------------------------------------------------------------------------------|
#   Started:        September 29th, 2020                                        |
#   Last Updated:   September 29th, 2020                                        |
#   Condition:      In progress                                                 |
#-------------------------------------------------------------------------------|
#   Time Spent Programming: 0 hour(s) 0 minute(s) 0 second(s)                   |
#-------------------------------------------------------------------------------|


import json
from os import system


# Load words from json file
wordDatabase    = open('words_dictionary.json')
dictionary      = []
wordCount       = 370100
currentCount    = 0

for word in json.load(wordDatabase):
    dictionary.append(word)
    currentCount += 1
    # Print percentage of words laoded
    print(f"\r{int((currentCount/wordCount)*100)}% of words loaded", end="")
print()
