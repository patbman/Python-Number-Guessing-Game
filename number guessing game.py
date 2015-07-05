from random import randint
def main():
	
	e,f = eval(input("what range do you want?: "))

	print("Im Thinking of a number between ",e," and ",f,"what is it?: ")

	a=""

	b = randint(e,f)
	count = 0
	while a != b:
		a = eval(input("guess your number: "))

		if a == b:
			print("You Got It Right")
			break
		elif a != b:

			count = count + 1
		if count >= 10:
			print("you have guessed wrong 10 times the correct answer was ", b)
			d = input("would you like to play again?(answer yes or no): ")
			if d == "yes":
				main()
			elif d == "no":
				break
main()


#By Patrick Bowden
