#!/usr/bin/python

# Mohammad Saad
# Hangman Game Solution
# 6/27/2015

from random import choice

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
		hang_tuple = createHangman()
		words = load_words(filename)

		self.currentWord = choice(words)

		self.guesses = []
		self.correctWords = ['_' for i in range(0, len(self.currentWord))]
		self.currentWordList = list(self.currentWord)

		self.state = 0

	def resetGame(self):
		self.currentWord = choice(words)

		self.guesses = []
		self.correctWords = ['_' for i in range(0, len(self.currentWord))]
		self.currentWordList = list(self.currentWord)

		self.state = 0

	

	def playGame(self):
	
		print "Welcome to Hangman!"
		person  = raw_input('Enter your name: ')
		print "Let's play Hangman, " + person + "!"



def main():
	h = Hangman("words.txt")
	h.playGame()

if __name__ == '__main__':
	main()
