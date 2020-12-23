import random
import time


def hang_the_player(count):
    if count == 1:
        print('\033[1;31;40m 4 tries remainning !! \033')
        print("    ________ \n"
              "   |         \n"
              "   |         \n"
              "   |         \n"
              "   |         \n"
              "   |         \n"
              "   |         \n"
              "___|___      \n")
    elif count == 2:
        print('\033[1;31;40m 3 tries remainning !! \033')
        print("    ________  \n"
              "   |        | \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "___|___       \n")
    elif count == 3:
        print('\033[1;31;40m 2 tries remainning !! \033')
        print("    ________  \n"
              "   |        | \n"
              "   |        | \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "___|___       \n")
    elif count == 4:
        print('\033[1;31;40m 1 try remainning !! \033')
        print("    ________  \n"
              "   |        | \n"
              "   |        | \n"
              "   |        | \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "___|___       \n")
    elif count == 5:
        print('\033[1;31;40m 0 try remainning !! \033')
        print("    ________  \n"
              "   |        | \n"
              "   |        | \n"
              "   |        | \n"
              "   |        0 \n"
              "   |          \n"
              "   |          \n"
              "___|___       \n")
    elif count == 6:
        print("\033[1;31;40m    ________  \n"
              "   |        |  \n"
              "   |        |  \n"
              "   |        |  \n"
              "   |        0  \n"
              "   |       /|\ \n"
              "   |       / \ \n"
              "___|___        \n")
        print('\033[1;31;40m **** GAME OVER ****')


def thats_correct(the_word, pl_guess):
    len_word = len(the_word)
    #use the find method to find the index of the guess letter
    pass

print('\n \033[1;32;40m  Hi there, Welcome to the Hangman game \n')
time.sleep(1.1337)
name = input('\033[0;37;40m Please enter your name : ')
time.sleep(1.1337)
print("\n   Let's begin the game {} !  GOOD LUCK and HAVE FUN :) \n".format(name))
time.sleep(1.1337)
print('   Remember to choose your letters wisely !! \n')
time.sleep(1.1337)
random_words = ['hello', 'world', name, 'beautiful', 'awesome', 'hangman', 'fun', 'game']
the_word = random.choice(random_words)
pl_guess = ''
print('\n This is the Hangman Word : {}   As you see it contains {} letters, Please enter your guess |only one letter per time|'.format('-'*len(the_word), len(the_word)))
count = 1
while 1:
    pl_guess = input('')
    if pl_guess not in the_word:
        hang_the_player(count)
        count += 1
    elif pl_guess in the_word:
        thats_correct(the_word, pl_guess)
    if count == 7:
        break