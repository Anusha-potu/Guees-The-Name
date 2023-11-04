import random
secret_word = random.choice(["Anusha.Potu","yazna","maggi","hel"])
print("Welcome to the guessing game!")
print("You have to guess the secret word. I will tell you how many letters it has.")
print("The secret word has", len(secret_word), "letters.")
guess = input("Please enter your guess: ")
while guess != secret_word:
    print("That's not correct. Try again!")
    guess = input("Please enter your guess: ")
print("Congratulations! You've guessed the secret word.")
