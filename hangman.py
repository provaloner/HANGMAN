import random
import string
print("H A N G M A N")
word_list = ['python', 'java', 'kotlin', 'javascript']
while True:
    command = input("Type \"play\" to play the game, \"exit\" to quit:")
    if command == "exit":
        break
    elif command == "play":
        word = random.choice(word_list)
        hint = "-" * len(word)
        attempts = 8
        win = 0
        guess_list = []

        while attempts > 0:
            print(f"\n{hint}")
            print(f"Attempts: {attempts}")
            guess = input("Input a letter:")
            if len(guess) != 1:
                    print("You should input a single letter")
                    continue
            else:
                if guess not in string.ascii_lowercase:
                    print("It is not an ASCII lowercase letter")
                    continue
                else:
                    if guess in guess_list:
                        print("You already typed this letter")
                        continue
                    else:
                        if guess in word:
                            for i in range(len(word)):
                                if word[i] == guess:
                                    hint = hint[:i] + guess + hint[i+1:]
                                    guess_list.append(guess)
                        else:
                            print("No such letter in the word")
                            attempts -= 1
                            guess_list.append(guess)
                        if hint == word:
                            win += 1
                            break
                        else:
                            continue

        if win == 1:
            print(f"You guessed the word {word}!")
            print("You survived!\n")
        else:
            print("You are hanged!\n")
