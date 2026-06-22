import random

while True:
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Guess a number between 1 and 100")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too Low!")
        elif guess > secret_number:
            print("Too High!")
        else:
            print("Congratulations! You guessed the number!")
            print("Attempts:", attempts)
            break

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break