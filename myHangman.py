#Hangman Game

import random

#user guesses a letter of a random word and they get 7 chances to get the word right
running = True
turnsLeft = 7
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
listOfWords = ["Placid", "Peaceful", "Calm", "Wonderful", "Brilliant", "Sexy"]
randomNumber = random.randint(1, len(listOfWords) - 1)
randomWord = str(listOfWords[randomNumber])
#randomWord = 'test'
randomWordGuessed = randomWord.lower()
currentGuessed = '_' * len(randomWord)



print('Welcome to a game of Hangman. You\'ll guess a letter each turn to try to guess a word.')
#loop of game
while running == True:
    #if the person guesses the word, show victory screen
    if currentGuessed == randomWord.lower():
        print(f'You got it! The word was {randomWord}. Congratulations!')
        running = False
        break
    #if they run out of guesses, show loss screen
    elif turnsLeft == 0:
        print(f'You\'ve run out of turns! The word was {randomWord}')
        running = False
        break
    else:
        print(f'You\'ve got {turnsLeft} turns left.')
    
    print(f'The word is {len(randomWord)} letters long.')
    #show the letters left to guess from
    print(f'You haven\'t guessed these letters: (if you have, try again because theres another of those letters in the word.)')
    print(' '.join(alphabet))
    #show current guess progress
    print(f'You\'ve currently guessed: {currentGuessed}')
    #guess the letter
    userLetter = input('Guess a letter: ')
    
    #check the result
    if userLetter in randomWordGuessed:
        #get index of which letter it is
        index = randomWordGuessed.index(userLetter)
        print("You guessed a letter in the word")
        currentGuessedLetters = []
        #rebuild the guessedletters list and the current guessed word
        for i, letter in enumerate(currentGuessed):
            #if letter is currently unguessed
            if letter == '_':
                #if on the index letter, add the letter
                if i == index:
                    letter = userLetter
                else :
                    letter = '_'
            currentGuessedLetters.append(letter)
        currentGuessed = ''.join(currentGuessedLetters)
        #do the opposite with the original word, taking out the letter guessed from it
        randomWordGuessedLetters = []
        for i, letter in enumerate(randomWordGuessed):
            if i == index:
                letter = '_'
            randomWordGuessedLetters.append(letter)
        randomWordGuessed = ''.join(randomWordGuessedLetters)
    else:
        print('That letter isn\'t in the word.')
        #increment the amount of turns left
        turnsLeft -= 1
    print()
    #remove the letter from the list of letters
    if userLetter in alphabet:
        if userLetter not in randomWordGuessed:
            alphabet.remove(userLetter)