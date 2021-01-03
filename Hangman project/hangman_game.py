import random
import time
import tools as tls

global pl_guess
global the_word
global hash_word


# print('\n \033[1;32;40m  Hi there, Welcome to the Hangman game \n')
# time.sleep(1.1337)
# name = input('\033[0;37;40m Please enter your name : ')
# tls.h_t_g()
# time.sleep(1.1337)
# print("\n \033[1;32;40m Let's begin the game\033[1;36;40m  {}".format(name))
# time.sleep(1.1337)
# random_words = ['hello', 'world', name, 'beautiful', 'awesome', 'hangman', 'fun', 'game', 'congratulation']
# the_word = random.choice(random_words)
# hash_word = '-'*len(the_word)


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
        print('\n\033[1;35;40m {} !!, {} more letter to win >[ {} ]< \n'.format(cngrts, hash_remaining,hash_word))
    else:
        print('\n\033[1;35;40m {} !!, {} more letters to win >[ {} ]< \n'.format(cngrts, hash_remaining,hash_word))


def re_load_the_game(check):
    global the_word
    global hash_word
    play_guess = 'y'
    if check:
        play_guess = input('\n\n\033[0;37;40m if you want to play again press y for [YES] else press any key to exit : ')
    if play_guess.lower() == 'y' or play_guess.lower() == 'yes':
        print('\nSTARTING NEW GAME ....')
        time.sleep(1.1337)
        the_word = random.choice(random_words)
        hash_word = len(the_word) * '-'
        print('\n This Is The New Hangman Word : {}   As you see it contains {} letters, Please enter your guess '.format(hash_word, len(the_word)))
        game_loop(random_words)
    elif play_guess.lower() == 'n' or play_guess:
        exit(0)


def game_loop(random_words):
    global the_word
    global hash_word
    count = 1
    while 1:
        pl_guess = input('\033[0;37;40m Enter your guess --> ')
        if pl_guess.lower() == 'help':
            tls.help_menu()
        elif pl_guess.lower() == 'rules':
            tls.h_t_g()
        elif pl_guess.lower() == 'restart':
            re_load_the_game(0)
        elif pl_guess.lower() == 'exit':
            exit(0)
        elif len(pl_guess) > 1 or not pl_guess.isalpha():
            print('\n\033[1;31;40m PLEASE ENTER ONE LETTER AT A TIME !\n type help for more information.\n')
            continue
        elif pl_guess not in the_word:
            tls.hang_the_player(count, the_word)
            count += 1
        elif pl_guess in the_word:
            thats_correct(pl_guess)
            if '-' not in hash_word:
                print('\n\033[1;32;40m *********** CONGRATULATION YOU WON !!! ***********\n')
                re_load_the_game(1)
        if count == 7:
            re_load_the_game(1)


if __name__ == "__main__":
    print('\n \033[1;32;40m  Hi there, Welcome to the Hangman game \n')
    time.sleep(1.1337)
    name = input('\033[0;37;40m Please enter your name : ')
    tls.h_t_g()
    time.sleep(1.1337)
    print("\n \033[1;32;40m Let's begin the game\033[1;36;40m  {}".format(name))
    time.sleep(1.1337)
    random_words = ['hello', 'world', name, 'beautiful', 'awesome', 'hangman', 'fun', 'game', 'congratulation', 'anime', 'football', 'movies', 'tvshows']
    the_word = random.choice(random_words)
    hash_word = '-'*len(the_word)
    print('\n \033[0;37;40m This is the Hangman Word : {}   As you see it contains {} letters, Please enter your guess '.format(hash_word, len(the_word)))
    game_loop(random_words)