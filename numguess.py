from random import randint
rand = randint(1, 100)
print("Welcome to this tech demo. You will try to guess a random number between 1 and 100.")
guess = int(input("Please enter an integer."))

while guess != rand:
    print("Unfortunately, your guess is wrong.")
    guess = int(input("Please try again."))
while rand == guess:
    print("Your guess is correct! Thank you for testing this tech demo.")
    stop = str(input("Please enter any kind of text to end this program."))