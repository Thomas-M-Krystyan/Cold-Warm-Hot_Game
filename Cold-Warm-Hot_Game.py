import os
import sys # to help exit the game
import random
from timeit import default_timer as timer


def random_number():
		number = random.sample(range(0, 9), 3)
		return tuple(number)

def clear(): # to clean the screen after each input
		if os.name == 'nt':
				os.system('cls') # Windows
		else:
				os.system('clear') # Linux / Mac OS

def help(): #to display help when needed
		clear()
		print('''Here are some clues:
+--------------+-------------------------------------------------+
| When I say:  |  That means:                                    |
+--------------+-------------------------------------------------+
| Cold         |  No digit is correct                            |
| Warm         |  One digit is correct but in the wrong position |
| Hot          |  One digit is correct and in the right position |
+--------------+-------------------------------------------------+
Type 'help' for help and 'quit' to exit the game.''')

def main():
		try:
				clear()
				print('I am thinking of a 3-digit number. Try to guess what it is.')
				help()
				lives = 0
				asking_for_answer = True
				
				while asking_for_answer: # difficulty loop
						decision_lives = input("\nChoose the diffuculty level:\n\n(E)asy    => 15 lives\n(M)edium  => 10 lives\n(H)ard    =>  5 lives\n\nI choose: ").lower()
						if decision_lives in ["easy", "e"]:
								lives = 15
								asking_for_answer = False
						elif decision_lives in ["medium", "m"]:
								lives = 10
								asking_for_answer = False
						elif decision_lives in ["hard", "h"]:
								lives = 5
								asking_for_answer = False
						elif decision_lives == 'help':
								help()
						elif decision_lives == 'quit':
							clear()
							sys.exit()
						else:
								clear()
								print("\nWrong option!")
				
				start = timer()
				number_tuple = random_number()
				chosen_number = str(number_tuple[0])+str(number_tuple[1])+str(number_tuple[2])
				guessesList = [] # a list with the guesses
				counter = 1
				clear()
				print('I have thought up a number. ', end='')
				while True: # game loop
						if bool(guessesList) == True: # printing the previous guesses to the screen
							print('You previous guesses are {}. '.format(guessesList), end='') 
						guess = input("You have {0} guesses to get it.\nGuess #{1}: ".format(lives, counter))
						guessesList.append(guess) #appending the guesses to the list
						clear()
						if guess == 'help':
							help()
							continue
						elif guess == 'quit':
							clear()
							sys.exit()
							continue
					
						if (len(guess) < 3) or (len(guess) > 3) or not intTryParse(guess):
								clear()
								print("\nERROR: Type 3 digits!")
								continue

						if guess == chosen_number:
								end = timer()
								print("\nYou got it in {0} seconds!".format(round((end - start), 2)))
								askUserIfContinue()

						answers = matching(chosen_number, guess)
						print("{} is > {} ".format(guess, ', '.join(answers)))
						lives -= 1

						if lives == 0:
								print("\nYou lost!!")
								askUserIfContinue()

						counter += 1
				
				input("Press any key to Exit")
				
		except BaseException as error:
				print(error)

def askUserIfContinue():
		decision = input("\nDo you want to play again? (yes or no): ")
		if decision.lower() in ["yes", "y"]:
				main()
		else:
				sys.exit() # to remove the none returning from the function

def intTryParse(value):
		try:
				int(value)
				return True
		
		except ValueError:
				return False

def matching(chosen_number, guess):
		answers = []
		hot_numbers = []
		warm_numbers = []
		
		h = 0
		while h < len(guess):
				if guess[h] == chosen_number[h]:
						answers.append("hot")
						hot_numbers.append(guess[h])
				h += 1

		w = 0
		while w < len(guess):
				if (guess[w] in chosen_number) and (guess[w] not in hot_numbers) and (guess[w] not in warm_numbers):
						answers.append("warm")
						warm_numbers.append(guess[w])
				w += 1

		if len(answers) == 0:
				answers = ["cold"]

		return answers

main()
