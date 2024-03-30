import time
import random


print("Welcome to Hangman Python!")
time.sleep(2)
print("You have to guess a random word in the dictionary in 7 tries.")
time.sleep(3)
print("Your word is being generated...")
time.sleep(4)


retry = "y"
while retry == "y":
    attempts = 7
    wordbank = ["ghost","water","face","chaos","fuel","jinx", "vex", "bump", "gym", "quiz", "flaw", "chef", "spy", "plow", "wok", "frog", "vamp", "quick", "jump", "quilt","waxy","hazed","subdermatoglyphic"]


    
    word = random.choice(wordbank)
    secret = "-"*len(word)
    secret_list = list(secret)
    #print(word)

    print("Word has been generated. Start guessing letters to find the word.")
    if word == "subdermatoglyphic":
        time.sleep(2)
        print("Hard Mode Enabled")

    while attempts > 0:
        guess = input("Guess a letter: ")
    

        if guess.lower() in word.lower():
            progress = secret_list[word.find(guess)] = guess
            secret = progress
            print("Correct!")
            print("Your word is",secret_list)

            if word == "".join(secret_list):
                print("You win! Your word was",word)
                time.sleep(2)
                retry = input("Try again? (y/n) ")
                break

        else:
            print("You lost an attempt,",attempts-1,"attempts remain")
            print("Your word is still",secret_list)
            attempts = attempts-1

            if attempts == 0:
                print("You lose! GG. Your word was",word)
                time.sleep(2)
                retry = input("Try again? (y/n) ")
                break