import random

print("Guess a number from 1 to 9 ")
number = random.randint(1,9)
def number_guess_game():
	chance = 1
	# While loop to count number chances
	while True:
		# Enter a number from 1 to 9
		guess = int(input("Enter the Number : "))
		# if guess number entered by user
		# that matches with generated randint function 
		# it break that loop and print the output
		if guess == number:
			print(f"CONGRATULATION! YOU HAVE GUESSED THE NUMBER {number} IN {chance} ATTEMPTS!")
			break
		# Checking if the user entered guess number was smaller than the generated number
		elif guess < number:
			print("Your guess was too low, Guess a number higher than %d" % guess)
		# Checking if the user entered guess number was higher than the generated number
		else:
			print("Your guess was too high, Guess a number less than %d" % guess)
		# Increase the value of chance by 1
		chance +=1

number_guess_game()
