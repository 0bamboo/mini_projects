import random
import time

print('\n \033[1;32;40m  Hi there, Welcome to the Hangman game \n')
time.sleep(2.1337)
name = input('\033[0;37;40m Please enter your name : ')
time.sleep(2.1337)
print("\n   Let's begin the game {} !  GOOD LUCK and HAVE FUN :) \n".format(name))
time.sleep(2.1337)
print('   Remember to choose your letters wisely !! \n')
time.sleep(2.1337)
random_words = ['hello', 'world', name, 'beautiful', 'awesome', 'hangman', 'fun', 'game']
the_word = random.choice(random_words)
print('\n This is the Hangman Word : {} Please enter your guess |only one letter per time|'.format('-'*len(the_word)))

