# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    count=0
    for letter in secret_word:
        if letter in letters_guessed:
            count=count+1
    if count==len(secret_word):
        return True
    else:
        return  False





def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    prtstr_list=list('-'*len(secret_word))
    index=0
    for letter in secret_word:
        if letter in letters_guessed:
           prtstr_list[index]=letter
        index=index+1
    return ''.join(prtstr_list)





def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabets=string.ascii_lowercase
    available_letter=[]
    for letter in alphabets:
        if letter not in letters_guessed:
            available_letter.append(letter)
    return ''.join(available_letter)


    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed=[]
    non_repeating_letters=no_of_nonrepeating_letters(secret_word)
    guessed_word=get_guessed_word(secret_word, letters_guessed)
    vowels=['a','e','i','o','u']
    guesses=6

    while(guesses!=0):
        warning=3

        while(warning!=0 and guesses!=0):

            print('_'*80)
            print("You have " +str(warning)+ " warnings left")
            print("\n The secret_word contains"+str(len(secret_word))+"letters and you have"+str(guesses)+"guesses left.")
            available_letters=get_available_letters(letters_guessed)
            print("\n Available letters: ", available_letters)
            print("\n Please guess a letter from available letters: ")

            input_letter=input()[0].lower()

            if input_letter in available_letters:
                letters_guessed.append(input_letter)
                guessed_word=get_guessed_word(secret_word, letters_guessed)
                if input_letter in vowels and input_letter not in secret_word:
                    vowels.remove(input_letter)
                    guesses=guesses-2
                    print("\n Oops! That letter is not in my word: ", guessed_word)
                    print_pic(guesses)
                    break

                if input_letter in secret_word:
                    print("\n Good guess: ",guessed_word)
                    break
                else:
                    guesses=guesses-1
                    print("\n Oops! That letter is not in my word: ", guessed_word)
                    print_pic(guesses)
                    break

            else:

                if input_letter.isalpha()==False:
                    guesses=guesses-1
                    print("\n Oops! You should give only alphabet: " +str(guessed_word)+"")
                    print_pic(guesses)
                    break
                elif input_letter in letters_guessed:
                    warning=warning-1
                    print("Oops! You've already guessed that letter. You now have "+ str(warning)+ " warnings: "+str(guessed_word))
                    if warning==0:
                     guesses=guesses-1
                     print_pic(guesses)
                     break

        if is_word_guessed(secret_word, letters_guessed):
            print("\n Congratulations, you won!")
            print("\n Your total score for this game is: " +str(guesses*non_repeating_letters))
            break
    if guesses==0:
        print("Sorry, you ran out of guesses. The word was else.")

    return





# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def no_of_nonrepeating_letters(secret_word):
    count=0
    for letter, i in zip (secret_word, range(len(secret_word))):
        if letter  not in secret_word[1+i:] and letter not in secret_word[0:i-1]:
            count=count+1
    return count


def print_pic(guesses):
    pic=[[[' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*']],
         [[' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*',' ','*',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ','*',' ',' ',' ','*',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*',' ','*',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*']],
         [[' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*',' ','*',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ','*',' ',' ',' ','*',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*',' ','*',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*']],
         [[' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*',' ','*',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ','*',' ',' ',' ','*',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*',' ','*',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ','*',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ','*',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*']],
         [[' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*',' ','*',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ','*',' ',' ',' ','*',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*',' ','*',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*','*','*',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ','*',' ','*',' ','*',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ','*',' ',' ','*',' ',' ','*',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*']],
         [[' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*',' ','*',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ','*',' ',' ',' ','*',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*',' ','*',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*','*','*',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ','*',' ','*',' ','*',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ','*',' ',' ','*',' ',' ','*',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*']],
         [[' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*',' ','*',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ','*',' ',' ',' ','*',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*',' ','*',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*','*','*',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ','*',' ','*',' ','*',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ','*',' ',' ','*',' ',' ','*',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ','*',' ','*',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ','*',' ',' ',' ','*',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ','*',' ',' ',' ',' ',' ','*',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*']]]
    prt_pic=pic[6-guesses]
    for row in range(16):
        print(''.join(prt_pic[row]))
    return



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    value=False
    index=0
    for x in my_word:
        if x!='-':
            if x == other_word[index]:
                value=True
            else:
                value=False
                break
        index=index+1
    return value



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    for other_word in wordlist:
        if match_with_gaps(my_word,other_word):
            print(other_word)







def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
