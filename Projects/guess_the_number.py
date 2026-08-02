## n students, they played this game there attempt we will save in the list/array then at the end of thr program we finally announce who is first winner, 2nd winner and 3rd winner

import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    number_to_guess = random.randint(1,100)
    attempt = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 to 100: "))
            attempt += 1
            if guess < number_to_guess:
                print("low! Try again.")
            elif guess > number_to_guess:
                print("high! Try again.")
            else:
                test = "Congrats! You got it in {} attempts!"
                print(test.format(attempt))
                print("The number is :",number_to_guess)
                return "Your are the winner"
        except ValueError:
            print("Please enter a valid integer.")

print(guess_the_number())