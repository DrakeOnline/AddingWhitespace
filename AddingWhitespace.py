#-------------------------------------------------------------------------------|
#   Title:          AddingWhitespace                                            |
#   Author:         Drake G. Cummings                                           |
#   Purpose:        Add correct whitespace to a file                            |
#-------------------------------------------------------------------------------|
#   Started:        September 29th, 2020                                        |
#   Last Updated:   September 29th, 2020                                        |
#   Condition:      In progress                                                 |
#-------------------------------------------------------------------------------|
#   Time Spent Programming: 1 hour(s) 20 minute(s) 58 second(s)                 |
#-------------------------------------------------------------------------------|


import json


# Load words from json file
wordDatabase    = open('words_dictionary.json')
dictionary      = []
wordCount       = 370100
currentCount    = 0

# load each word in the databse into a list for quicker checking
for word in json.load(wordDatabase):
    dictionary.append(word)
    currentCount += 1
    # Print percentage of words laoded
    print(f"\r{int((currentCount/wordCount)*100)}% of words loaded", end="")
print()


# Add spaces after every punctuation
punctuation     = ['.', '!', '?', ',', ':', ';']
originalFile    = open('Newtext.txt','r')
newString       = ""

# Get each line
for line in originalFile:

    # Get each character in each line
    for character in line:
        newString += character

        # Check each character in the line with each punctuation mark
        for mark in punctuation:
            if character == mark:
                newString += " "


# Write string with new spacing to temporary file
newFile = open('tmp.txt', 'w')
newFile.write(newString)
newFile.close()
