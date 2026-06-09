import random
words = ["python", "java", "computer", "engineer", "laptop", "code"]
word = random.choice(words)
chance = 6
show_word = ["_"] * len(word)

print("Welcome to HangMan!")
print("The secret word had ", len(word)," Letters")
print(" ".join(show_word))
print("_" * 20)

while chance > 0 and "_" in show_word :
    guess = input("Guess a letter: ").lower()
    if guess in word :
        print(f"Good Job! '{guess}' is in the word.")
        for i in range(len(word)):
            if word[i] == guess :
                show_word[i] = guess
    else :
        chance -= 1
        print(f"Wrong guess '{guess}' is not in word.")
        print(f"You have '{chance}' turns left!.")
    
    print(" ".join(show_word))
    print("_" * 20)
if "_" not in show_word:
    print("🎉 Congratulations! You guessed the word and WON the game! 🎉")
else:
    print(f"💀 Game Over! You ran out of turns. The secret word was '{word}'.")