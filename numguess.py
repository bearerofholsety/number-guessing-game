from random import randint

print("Welcome to this tech demo. You will try to guess a random number between 1 and 100.\n")

rand = randint(1, 100)

def game():
  try:
    
    guess = int(input("Please enter an integer.\n"))
  
  except ValueError:
    print("Enter a number please.")
    game() # goes back until a number is entered.
  #print(rand) for debugging purposes
  
  if rand != guess: #No need for loop if you got function
    print("Unfortunately, your guess is wrong.")
    game()
  
  else: #you can do "elif rand == guess" but "else" is a more nice thing
    print("Your guess is correct! Thank you for testing this tech demo.")
    exit(2) #Quits program without errors
game()    
