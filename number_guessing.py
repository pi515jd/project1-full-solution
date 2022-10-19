import random

while True:

    boolean = True
    while boolean:
        num = input("Type a number for an upper bound: ")
        if num.isdigit():
            print("Let's play!")
            num = int(num)
            boolean = False
        else:
            print("Invalid input. Try again.")

    secret = random.randint(1, num)
    guess = None
    count = 1

    while guess != secret:
        guess = input("Type a number between 1 and " + str(num) + ": ")
        if guess.isdigit():
            guess = int(guess)
        if guess == secret:
            print("You got it!")
        else:
            print("Try again.")
            count += 1

    if count == 1:
        print("It took you", count, "guess!")
    else:
        print("It took you", count, "guesses!")
