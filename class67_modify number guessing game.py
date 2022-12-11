guessing_number=67
guess=1
n=int(input("Guess a number between 1 to 100: "))
game_over=False

while not game_over:
    if n == guessing_number:
        print(f"You have correctly guesses he number in {guess} times")
        game_over=True
    else:
        if n<guessing_number:
            print(f"too low, guess again")
            guess+=1
            n=int(input())
        else:
            print("Too high, guess again") 
            guess+=1
            n=int(input())   

            
