#The Hangman Game

import random, time, os, pyfiglet

# Lists
listOfWords = ['stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']
HangmanPics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Subroutine to get a random word for the game
def getRandomWord(listOfWords):
  return random.choice(listOfWords)

#Main loop
while True:
  title = pyfiglet.figlet_format("The Hangman Game")
  print(title)
  time.sleep(2)
  
  print()
  
  secretWord=getRandomWord(listOfWords)
  correctLetter=[]
  missedLetter=[]
  gameIsDone=False

  #Subroutine to display the board
  def displayBoard(missedLetters, correctLetters, secretWord):
    print("\033[36m", HangmanPics[len(missedLetters)], "\033[0m")
    print()
    for letter in secretWord:
      for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
          print(secretWord[i], end="")
        else:
          print("_", end="")
      return letter

  #Game loop
  while not gameIsDone:
    os.system("clear")
    displayBoard(missedLetter,correctLetter,secretWord)
    
    print("\n\n")

    #User's input
    chosenLetter=input("\033[33m Choose a letter > \033[0m").strip().lower()
    
    if len(chosenLetter) != 1:
      print("Please enter a single letter")
      time.sleep(1)
    elif chosenLetter in missedLetter or chosenLetter in correctLetter:
      print("You have already chosen that letter")
      time.sleep(1)
    else:
      if chosenLetter in secretWord:
        correctLetter.append(chosenLetter)
        print("Very well!")
        time.sleep(1)
      else:
        missedLetter.append(chosenLetter)
        print(f"Wrong letter. You have {6-len(missedLetter)} tries left")
        time.sleep(1)
        
    correctWord=all(letter in correctLetter for letter in secretWord)
    if correctWord:
      displayBoard(missedLetter,correctLetter,secretWord)
      print()
      print("You've won!")
      gameIsDone=True

    if len(missedLetter)>5:
      os.system("clear")
      displayBoard(missedLetter,correctLetter,secretWord)
      print()
      print("Sorry, you lost; the correct word was: ", secretWord)
      break
  
  print()
  
  again=input("Do you want to play again? (yes or no) > ").strip().lower()
  if again!="yes":
    break
