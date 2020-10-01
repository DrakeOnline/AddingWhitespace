#-------------------------------------------------------------------------------|
#   Title:          Utils                                                       |
#   Author:         Drake G. Cummings                                           |
#   Purpose:        Helper functions for AddingWhitespace file                  |
#-------------------------------------------------------------------------------|

# Function for finding all words in a string
def FindAllWords(callCount, phrase, dictionary, sentences):
    sentences[callCount] = []
    word = ""

    for count in range(0, len(phrase)):
        # Add one character at a time
        word += phrase[count].lower()

        # Check if current sentence is in the dictionary
        if word in dictionary:
            sentences[callCount].append(word)
            sentences.append([])
            FindAllWords(callCount, phrase[(count+1):], dictionary, sentences)
