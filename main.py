import random 
randNumber = random.randint(1, 100)
#print(randNumber)
userGuess = None
guesses = 0
while(userGuess != randNumber):
    userGuess = int(input("Enter your Guess: "))
    guesses +=1
    if (userGuess == randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Please enter a smaller number")
        else:
            print("You uessed it wrong! Please enter a larger number")    
       

print(f"You guessed the number in {guesses} guesses") 
with open ("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if (guesses<hiscore):
    print("You have just broken the highscore!")    
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
