# !/bin/python

def hang_the_player(count):
    if count == 1:
        print('\n\033[1;31;40m 4 tries remainning !! \n')
        print("    ________ \n"
              "   |         \n"
              "   |         \n"
              "   |         \n"
              "   |         \n"
              "   |         \n"
              "   |         \n"
              "___|___      \033\n")
    elif count == 2:
        print('\n\033[1;31;40m 3 tries remainning !! \n')
        print("    ________  \n"
              "   |        | \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "___|___       \033\n")
    elif count == 3:
        print('\n\033[1;31;40m 2 tries remainning !! \n')
        print("    ________  \n"
              "   |        | \n"
              "   |        | \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "___|___       \033\n")
    elif count == 4:
        print('\n\033[1;31;40m 1 try remainning !! \n')
        print("    ________  \n"
              "   |        | \n"
              "   |        | \n"
              "   |        | \n"
              "   |          \n"
              "   |          \n"
              "   |          \n"
              "___|___       \033\n")
    elif count == 5:
        print('\n\033[1;31;40m 0 try remainning !! \n')
        print("    ________  \n"
              "   |        | \n"
              "   |        | \n"
              "   |        | \n"
              "   |        0 \n"
              "   |          \n"
              "   |          \n"
              "___|___       \033\n")
    elif count == 6:
        print('\n\033[1;31;40m YOU DIED :( !! \n')
        print("\n\033[1;31;40m    ________  \n"
              "   |        |  \n"
              "   |        |  \n"
              "   |        |  \n"
              "   |        0  \n"
              "   |       /|\ \n"
              "   |       / \ \n"
              "___|___        \n")
        print('\n\n\033[1;31;40m **** GAME OVER ****\n\n\n')


def help_menu():
    print("\n           HELP  :              \n"
          "\n help : for help menu .\n"
          "\n restart : for reload the game .\n"
          "\n rules : for explain how to play the game .\n"
          "\n exit : for quit the game .\n")


def h_t_g():
    print("  \n Welcome to the hangman game ,\n" 
            "   the rules are sample we gonna randomly choose a word,\n"
            "   and you gonna try to guess that word by entering one letter per time,\n"
            "   remember one letter per time !! \n"
            "   you only have 6 tries so try to choose your letters wisely \n")