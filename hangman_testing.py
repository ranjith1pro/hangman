import random
import string

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_list=[]
	value=False
    # FILL IN YOUR CODE HERE AND DELETE "pass"
	for other_word in wordlist:
		if match_with_gaps(my_word,other_word):
			list.append(other_word)
			print(other_word)
			value=True
	if value==True:
		wordlist=word_list
    pass



secret_word='ranjith'
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
                print_pic(guesses)
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
                print("\n Oops! You've already guessed that letter. You now have "+ str(warning)+ " warnings: "+str(guessed_word))
                if warning==0:
                    guesses=guesses-1
                    print_pic(guesses)
                    break

    if is_word_guessed(secret_word, letters_guessed):
        print("\n Congratulations, you won!")
        print("\n Your total score for this game is: " +str(guesses*non_repeating_letters))
        break
if guesses==0:
    print("\n Sorry, you ran out of guesses. The word was else.")









