#-------------------------------------------------------------------------------|
#   Title:          Utils                                                       |
#   Author:         Drake G. Cummings                                           |
#   Purpose:        Helper functions for AddingWhitespace file                  |
#-------------------------------------------------------------------------------|

# Function for finding all words in a string
def FindAllWords(phrase, dictionary):

    word = ""

    for count in range(0, len(phrase)):
        word += phrase[count].lower()

        # Check if current sentence is in the dictionary
        if word in dictionary:
            print(f"Word found: {sentence}")
            FindAllWords(phrase[(count+1):], dictionary)

    return sentence
