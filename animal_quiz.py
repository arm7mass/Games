
def check_guess(guess, answer):
    global score
    still_gessing = True
    attempt = 0 
    while still_gessing and attempt < 3 :
        if guess.lower() == answer.lower():
            print("Correct aswer")
            score = score +1
            still_gessing = False
        else:
            if attempt < 2 :
                guess = input("Sorry wrong answer try again  ")
            attempt = attempt + 1
    
    if attempt == 3:
        print(f'the correct answer is {answer}')

score = 0
print(" Guess the animal " )

guess1 = input("which the fatest land animal ?")
check_guess(guess1, "cheetah")

guess2 = input("which bear lives at the north Pole?")
check_guess(guess2, "Polar bear")


guess3 = input("which the largest animal ?")
check_guess(guess3, "blue whale")

print(f" Your score is {score}")








