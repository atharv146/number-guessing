import random 
number = int(random.randint(1,100))
print("You will have 5 guesses to guess the number correctly.")
guess = int(input("Guess the number: "))
numguess = 1
hintnumber1 = number - int(random.randint(5,10))
hintnumber2 = number + int(random.randint(5,10))
while True:
    
    if numguess == 5:
        print("This is your last guess so as a hint the number is between",hintnumber1,"and",hintnumber2)
        guess = int(input("Final attempt to guess the number: "))
        numguess = numguess + 1
    if numguess == 6:
        print("That is wrong meaning you have lost the game. Womp Womp u suck.")
        break
    if guess < number: 
        print("Your guess is too low. Try again.")
        guess = int(input("Guess the number: "))
        numguess = numguess + 1
        
    elif guess > number: 
        print("Your guess is too high. Try again.")
        guess = int(input("Guess the number: "))
        numguess = numguess + 1
    
    elif guess == number:
        print("Congrats", number, "is correct.")
        print("You guessed it in", numguess, "tries.")  
        break   
    