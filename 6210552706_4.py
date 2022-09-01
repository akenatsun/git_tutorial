word = "Akenat"
tries = 6
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")
    
    guess = input(f"trial: {tries}, Guess letter: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        print("Don't have letter  ")
        tries -= 1
        if tries == 0:
            break
    
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False
            
if done:
    print("Done")

else:
    print(f"die")
