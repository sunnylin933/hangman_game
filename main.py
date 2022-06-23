import random
import art
from word_lists import food_list, city_list

playing = True
current_stage = 6
guessed_letters = []
incorrect_letters = []

game_type_response = input("Welcome to Hangman! Please pick from one of the following categories: Foods, Cities ").lower()
if any(game_type_response == response for response in ['foods', 'food', 'f', '0']):
    game_type = food_list
elif any(game_type_response == response for response in ['cities', 'city', 'c', '1']):
    game_type = city_list

chosen_word = random.choice(game_type) 
word_state = ["_"] * len(chosen_word)

#Removes spaces
if(" " in chosen_word):
    for i in range(len(chosen_word)):
        if(chosen_word [i] == " "):
            word_state[i] = " "

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

        if(guessed_letter == " " or len(guessed_letter) > 1):
            print("Invalid Response.")
        elif(guessed_letter in guessed_letters):
            print("Letter already guessed.")
        elif(guessed_letter != " " and guessed_letter in chosen_word):
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