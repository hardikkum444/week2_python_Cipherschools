import random
guessing_number = random.randint(1,100)
guess=1
n=int(input("Guess a number between 1 to 100: "))
game_over=False

while not game_over:
    if n == guessing_number:
        print(f"You have correctly guessed the number in {guess} times")
        game_over=True
    else:
        if n<guessing_number:
            print(f"too low, guess again")
           
        else:
            print("Too high, guess again") 
            
        guess+=1
        n=int(input())
            
            
