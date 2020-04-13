import random

def generate_random_word():
    words="chair blanket dog flower lamp horse house picture photo unicorn phone window cup candy remote book zoom spoon trash panda sloth".split()
    word=random.choice(words)
    return word

def play_hangman():
    playing = True


    while (playing):
        guessed_letters = []
        correct_letters = []
        guesses_left = 10
        word = generate_random_word()
        letter = input("Pick a letter:")
        done = False
        while not done or guesses_left>0:
            if letter in guessed_letters:
                guesses_left-=1 #subtract one from guesses_left
                print("You have already guessed the letter",letter,".") #and tell them they already guessed that letter
            elif letter not in list(word):
                guessed_letters+=letter #add letter to guessed letters
                print(letter,"is not in the word.") #tell user the letter is not in the word
                guesses_left-=1 #subtract one from the guesses_left
                print("You have guessed:",guessed_letters)
                print("You have",guesses_left,"guesses left.")
            else:
                guessed_letters+=letter #add letter to guessed letters
                correct_letters+=letter
                print(letter,"is in the word!") #tell user the letter is in the word
                print("You have guessed:",guessed_letters)
                print("You have",guesses_left,"guesses left.")
            if guesses_left==0: #the number of guesses left is zero
                done=True #set done to be true and tell the user they lost!
                print("You ran out of guesses. Sorry, you lost :(")
            else:
                dashes = []
                for d in word:
                    if d in guessed_letters:
                        dashes += d
                    else:
                        dashes += '-'
                print(dashes)
                print()
            foundAllLetters = True
            for i in range(len(word)):
                if word[i] not in correct_letters:
                    foundAllLetters = False
                    letter = input("Pick a letter:") #ask the user for another letter
                    break
            if foundAllLetters:
                print("The word was",word+". Congrats, you guessed it correctly!") 
                done=True
                break
        want_to_play = input("Would you like to play again?[yes]/[no]")#ask the user if they want to play another game...
        if want_to_play=="yes":
            playing=True
        elif want_to_play=="no":
            playing=False
            print("Thank you for playing!")

if __name__ == '__main__':
    play_hangman()
