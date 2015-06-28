#!/usr/bin/python

# Mohammad Saad
# Hangman Game Solution
# 6/27/2015

from random import choice
from sets import Set

def load_words(filename):
	words = []
	with open(filename, 'r') as f:
		words.append(f.readline())

	return words

def createHangman():
	HANGMAN = (

'''

| |

|

|

|

|

|

''',

'''

| |

| O

|

|

|

|


''',

'''

| |

| O

| |

| |

|

|


''',

'''


| |

| O

| |_

| |

|

|


''',

'''


| |

| O

| _|_

| |

|

|


''',

'''


| |

| O

| _|_

| |

| /

|


''',

'''


| |

| O

| _|_

| |

| / \\

|


'''

)
	return HANGMAN

class Hangman():

	def __init__(self, filename):
		# create our hangman and word list
		self.hang_tuple = createHangman()
		self.words = load_words(filename)

		# define letters you are allowed to use
		self.allowed_letters = allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

		# pick a word
		self.currentWord = choice(self.words)

		# create an array of guesses to see if we have guessed it before
		self.guesses = []
		self.correctLetters = ['_' for i in range(0, len(self.currentWord))]
		self.currentLetterList = list(self.currentWord)

		# state keeps track of how many incorrect guesses
		self.state = 0

	def resetGame(self):
		# reset everything from above, no need to load file again
		self.currentWord = choice(self.words)

		self.guesses = []
		self.correctLetters = ['_' for i in range(0, len(self.currentWord))]
		self.currentLetterList = list(self.currentWord)

		self.state = 0

	def makeGuess(self, letter):
		letter = letter.lower()

		if letter not in self.allowed_letters:
			print "Not an allowed letter!"
			return

		letter_in_list = False

		for i in range(0, len(self.currentLetterList)):
			if letter == self.currentLetterList[i]:
				letter_in_list = True
				self.correctLetters[i] = letter



		if letter_in_list:
			print "There was an " + letter + " in the word! Good job!"
		else:
			print "There was no " + letter + " in the list. Sorry!"
			self.state += 1

	def endGame(self):
		if "_" not in self.correctLetters:
			print "Congratulations! You guessed the word {0}!".format(self.currentWord)
		elif (self.state < len(self.hang_tuple) - 1):
			print "You lost. The word was {0}.".format(self.currentWord)
			print self.hang_tuple(state)
		else:
			return 2

		playAgainBool = raw_input("Play again? (y/n): ")

		while(playAgainBool != 'y' or playAgainBool != 'n'):
			playAgainBool = raw_input("Play again? (y/n): ")

		if(playAgainBool == 'y'):
			return 1
		else:
			return 0




	def playGame(self):
	
		self.resetGame()

		print "Welcome to Hangman!"
		person  = raw_input('Enter your name: ')
		print "Let's play Hangman, " + person + "!"

		while(self.state < len(self.hang_tuple)):

			for i in range(0, len(self.correctLetters)):
				print self.correctLetters[i]

			print self.hang_tuple[self.state]

			guess = raw_input("Enter a letter to guess: ")

			self.makeGuess(letter)

			again = self.endGame()

			if(again == 2):
				continue
			elif again == 1 or again == 0:
				break

		if(again == 1):
			playGame()








def main():
	h = Hangman("words.txt")
	h.playGame()

if __name__ == '__main__':
	main()
