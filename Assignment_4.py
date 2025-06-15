import random

words = ['apple', 'bread', 'candy', 'dream', 'eagle', 'flame', 'grape', 'house', 'input', 'joker']

def possible_errors(tries, length):
    try:
        user_word = input(f'Attempt {7 - tries}/6 – Enter guess: ').lower()
        if len(user_word) != length:
            print(f'Wrong length. Expected {length}')
            return None
    except Exception as e:
        print(f'Unexpected error {e}')
        return None
    return user_word

def letters_in_word(secret_word, user_word):
    display_list = []
    for i in range(len(secret_word)):
        if user_word[i] == secret_word[i]:
            display_list.append(f' [{user_word[i].upper()}] ')
        elif user_word[i] in secret_word:
            display_list.append(f' ({user_word[i]}) ')
        else:
            display_list.append(f' {user_word[i]} ')
    print("Result:", ' '.join(display_list))

def play_wordle():
    secret_word = random.choice(words)
    length = len(secret_word)
    tries = 6
    print(f'Guess the {length}-letter word. You have {tries} tries.')
    while tries > 0:
        user_word = possible_errors(tries, length)
        if user_word is None:
            continue
        if user_word == secret_word:
            print("You win!!!")
            break
        letters_in_word(secret_word, user_word)
        tries -= 1
    else:
        print(f'You lose! The word was: {secret_word}')

def loop_play_wordle():
    print("Welcome to Wordle!")
    while True:
        play_wordle()
        next_play = input("Do you want to play one more time? Print yes or no: ").lower()
        if next_play != "yes":
            print("Thanks for being here! See you soon)")
            break

loop_play_wordle()
