import random

def play_tournament():
    print("Welcome to the N-player Random Battle!".upper())

    try:
        n = int(input("Enter the total number of student you want to participation: "))
    except ValueError:
        print("Please enter a valid integer for number of students.")

    if n < 3:
        print("You need at least 3 students to award all three places, 1st, 2nd and 3rd ")
        return 
    
    attempt_of_each_students = []

    for i in range(1,n+1):
        print("---- Player {i}'s Turn ----")
        name = input("Enter the name of student: ")
        print("Welcome to the Guess the Number Game!")
        number_to_guess = random.randint(1,50)
        attempt = 0

        print("Hey {name}! I have picked a secret number between 1 to 50, Try to guess this number with least attempt to win the game")

        while True:
            try:
                guess = int(input("Guess a number between 1 to 50: "))
                attempt += 1
                if guess < number_to_guess:
                    print("low! Try again.")
                elif guess > number_to_guess:
                    print("high! Try again.")
                else:
                    test = "Congrats! You got it in {} attempts!"
                    print(test.format(attempt))
                    print("The number is :",number_to_guess)
                    break
            except ValueError:
                print("Please enter a valid integer.")
        attempt_of_each_students.append([name,attempt])
        attempt_of_each_students.sort(key=lambda x : x[1])
    
    print(" Tournament Over! Final Ranking .....".upper())

    model = ["1st Winner", "2nd Winner", "3rd Winner"]

    for i in range(1,4):
        print("{i} Winner is: ",attempt_of_each_students[i-1][0])


play_tournament()






        
