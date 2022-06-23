import random
import art
from word_lists import valid_letters, food_list, city_list

genre_chosen = False
playing = True
current_stage = 6
guessed_letters = []
incorrect_letters = []

print(art.logo)
game_type_response = print("\nWelcome to Hangman!")

#Player Genre Choice
while(not genre_chosen):
    game_type_response = input("Please pick from one of the following categories: Foods, Cities").lower()
    genre_chosen = True
    if any(game_type_response == response for response in ['foods', 'food', 'f', '0']):
        game_type = food_list
        print("You selected foods!")
    elif any(game_type_response == response for response in ['cities', 'city', 'c', '1']):
        game_type = city_list
        print("You selected cities!")
    else:
        print("Invalid Response.")
        genre_chosen = False

chosen_word = random.choice(game_type) 
word_state = ["_"] * len(chosen_word)

#Player Letter Choice
##Removes spaces
if(" " in chosen_word):
    for i in range(len(chosen_word)):
        if(chosen_word [i] == " "):
            word_state[i] = " "

##Checks choice
while(playing):
    print(art.stages[current_stage])
    if(not "_" in word_state):
        playing = False
        print("You Win! Your word was: " + chosen_word)
    elif(current_stage == 0):
        playing = False
        print("You Lose! Your word was: " + chosen_word)
    else:
        print("".join(word_state))

        guessed_letters_string = ", ".join(guessed_letters)
        print(f"\nGuessed Letters: {guessed_letters_string}")

        guessed_letter = input("Choose a letter: ").lower()

        if(not guessed_letter in valid_letters or len(guessed_letter) > 1): #checks to see if guess is valid
            print("Invalid Response.")
        elif(guessed_letter in guessed_letters): #checks to see if guess has already been guessed
            print("Letter already guessed.")
        elif(guessed_letter != " " and guessed_letter in chosen_word): #checks to see if guess is in chosen word
            for i in range(len(chosen_word)):
                if chosen_word[i] == guessed_letter:
                    word_state[i] = guessed_letter  
            guessed_letters += guessed_letter
            print("Correct Guess!\n")
        else:
            current_stage -= 1
            incorrect_letters += guessed_letter
            incorrect_letters_string = ", ".join(incorrect_letters)
            print(f"Incorrect Guess!")