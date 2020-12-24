import random
import time

global pl_guess
global the_word
global hash_word
print('\n \033[1;32;40m  Hi there, Welcome to the Hangman game \n')
time.sleep(1.1337)
name = input('\033[0;37;40m Please enter your name : ')
time.sleep(1.1337)
print("\n   Let's begin the game {} !  GOOD LUCK and HAVE FUN :) \n".format(name))
time.sleep(1.1337)
print('   Remember to choose your letters wisely !! \n')
time.sleep(1.1337)
random_words = ['hello', 'world', name, 'beautiful', 'awesome', 'hangman', 'fun', 'game', 'congratulation']
the_word = random.choice(random_words)
hash_word = '-'*len(the_word)

def hang_the_player(count):
    if count == 1:
        print('\033[1;31;40m 4 tries remainning !! \n')
        print("    ________ \n"
              "   |         \n"
              "   |         \n"
              "   |         \n"
              "   |         \n"
              "   |         \n"
              "   |         \n"
              "___|___      \033\n")
    elif count == 2:
        print('\033[1;31;40m 3 tries remainning !! \n')
        print("    ________  \n"
              "   |        | \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "___|___       \033\n")
    elif count == 3:
        print('\033[1;31;40m 2 tries remainning !! \n')
        print("    ________  \n"
              "   |        | \n"
              "   |        | \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "___|___       \033\n")
    elif count == 4:
        print('\033[1;31;40m 1 try remainning !! \n')
        print("    ________  \n"
              "   |        | \n"
              "   |        | \n"
              "   |        | \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "___|___       \033\n")
    elif count == 5:
        print('\033[1;31;40m 0 try remainning !! \n')
        print("    ________  \n"
              "   |        | \n"
              "   |        | \n"
              "   |        | \n"
              "   |        0 \n"
              "   |          \n"
              "   |          \n"
              "___|___       \033\n")
    elif count == 6:
        print("\033[1;31;40m    ________  \n"
              "   |        |  \n"
              "   |        |  \n"
              "   |        |  \n"
              "   |        0  \n"
              "   |       /|\ \n"
              "   |       / \ \n"
              "___|___        \n")
        print('\n\n\033[1;31;40m **** GAME OVER ****\n\n\n')

def menu():
    pass


def thats_correct(pl_guess):
    global hash_word
    global the_word
    index = the_word.find(pl_guess)
    the_word = the_word[:index] + '-' + the_word[index + 1:]
    hash_word = hash_word[:index] + pl_guess + hash_word[index + 1:]
    hash_remaining = hash_word.count('-')
    good = ['GOOD', 'NICE', 'PERFECT', 'AWESOME']
    cngrts = random.choice(good)
    if hash_remaining == 1:
        print('\n\033[1;35;40m {} GUESS , {} more letter >[ {} ]< KEEP IT UP \n'.format(cngrts, hash_remaining,hash_word))
    else:
        print('\n\033[1;35;40m {} GUESS , {} more letters >[ {} ]< KEEP IT UP \n'.format(cngrts, hash_remaining,hash_word))


def game_loop(random_words):
    global the_word
    global hash_word
    count = 1
    while 1:
        pl_guess = input('\033[0;37;40m Enter your guess --> ')
        if len(pl_guess) > 1 or not pl_guess.isalpha():
            print('PLEASE ENTER ONE LETTER AT A TIME !')
            continue
        if pl_guess not in the_word:
            hang_the_player(count)
            count += 1
        elif pl_guess in the_word:
            thats_correct(pl_guess)
            if '-' not in hash_word:
                print('\n\033[1;32;40m *********** CONGRATULATION YOU WON !!! ***********\n')
                play_guess = input('\033[0;37;40m if you want to play again press y [YES] if not press n [NO] : ')
                if play_guess.lower() == 'y':
                    print('\nSTARTING NEW GAME ....')
                    time.sleep(1.1337)
                    the_word = random.choice(random_words)
                    hash_word = len(the_word) * '-'
                    print('\n This Is The New Hangman Word : {}   As you see it contains {} letters, Please enter your guess |only one letter per time|'.format(hash_word, len(the_word)))
                    game_loop(random_words)
                elif play_guess.lower() == 'n' or play_guess:
                    break
        #  SOMETHING IS WRONG HERE FIX IT !!!!!!!
        if count == 7:
            play_guess = input('\033[0;37;40m if you want to play again press y [YES] if not press n [NO] : ')
            if play_guess.lower() == 'y':
                print('\nSTARTING NEW GAME ....')
                time.sleep(1.1337)
                the_word = random.choice(random_words)
                hash_word = len(the_word) * '-'
                print('\n This Is The New Hangman Word : {}   As you see it contains {} letters, Please enter your guess |only one letter per time|'.format(hash_word, len(the_word)))
                game_loop(random_words)
            elif play_guess.lower() == 'n' or play_guess:
                break

print('\n This is the Hangman Word : {}   As you see it contains {} letters, Please enter your guess |only one letter per time|'.format(hash_word, len(the_word)))
game_loop(random_words)