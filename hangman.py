import random
words = ["counselor", "dinosaur", "heliport", "breakfast", "entrepreneur"]
list_of_used_chars = []
lives = 6


def pick_word(my_list):
    word_to_guess = random.choice(my_list)
    number = len(word_to_guess)
    i = 0
    some_list = []
    while i < number:
        some_list.append("_")
        i += 1
    return word_to_guess, some_list


def gimme_letter():
    letter = input("Tell me your letter: ")
    letter = letter.lower()
    return letter


def validate_letter(letter):
    num = len(letter)
    if num > 1:
        return False
    return letter.isalpha()


def check_list(letter, list_of_used_letters):
    return letter in list_of_used_letters


def check_letter(letter, list_of_used_letters, word_to_guess, some_list, alive):
    list_of_used_letters.append(letter)
    if letter in word_to_guess:
        print("This letter is indeed in the word")
        i = 0
        for n in word_to_guess:
            if n == letter:
                some_list[i] = letter
            else:
                pass
            i += 1
        print(some_list)
    else:
        alive -= 1
        print(f"This letter is not in the word - you have {alive} live(s) left.")
    return list_of_used_letters, some_list, alive


def won_or_not(alive, some_list):
    if alive == 0:
        print("You lost.")
        return True
    if "_" not in some_list:
        print("Congrats - you won.")
        return True
    else:
        return False


hidden_word, riddle = pick_word(words)
print("I have picked the word. Try to guess it")
print(riddle)
while lives > 0:
    my_letter = gimme_letter()
    while not validate_letter(my_letter) or check_list(my_letter, list_of_used_chars):
        if not validate_letter(my_letter):
            print("That's not a letter")
        else:
            print("You've already given me this letter")
        my_letter = gimme_letter()
    list_of_used_chars, riddle, lives = check_letter(my_letter, list_of_used_chars, hidden_word, riddle, lives)
    if won_or_not(lives, riddle):
        break
    else:
        pass
