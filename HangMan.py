v_hangman = (
        """
        -----
        |    |
        |    O
        |
        |
        |
        |
        |
        ---------
        """,
        """
        -----
        |    |
        |    O
        |    |
        |    |
        |
        |
        |
        ---------
        """,
        """
        -----
        |    |
        |    O
        |   /|
        |  / |
        |
        |
        |
        ---------
        """,
        """
        -----
        |    |
        |    O
        |   /|\\
        |  / | \\
        |
        |
        |
        ---------
        """,
        """
        -----
        |    |
        |    O
        |   /|\\
        |  / | \\
        |   /
        |  /
        |
        ---------
        """,
        """
        -----
        |    |
        |    O
        |   /|\\
        |  / | \\
        |   / \\
        |  /   \\
        |
        ---------
        """,
        """
        -----
        |    |
        |    O
        |   /|\\
        |  / | \\
        |   / \\
        | _/   \\
        |
        ---------
        """,
        """
        -----
        |    |
        |    O
        |   /|\\
        |  / | \\
        |   / \\
        | _/   \\_
        |
        ---------
        """
    )


def is_letter_exists(v_let):
    global v_mark
    for i in range(len(v_word)):
        if v_word[i] == v_let:
            v_mark_lst[i] = v_let
            v_mark = "".join(v_mark_lst)


def check_if_win():
    global v_count_games
    if '-' not in v_mark_lst:
        v_count_games += 1
        print("NOICE! You did it with {} failures.\n".format(v_counter))
        return True


def check_if_fail():
    global v_count_games
    if '-' in v_mark_lst:
        v_count_games += 1
        print("HAHAHIHI! You didn't do it and the man is hanged and dead!!!\n")
        print("The word is: {}".format(v_word))


def is_letter_doesnt_exist(v_let):
    global v_counter
    if v_let not in v_word:
        print('There is no "'"{}"'" in the word.'.format(v_let))
        print(v_hangman[v_counter])
        v_counter += 1
    return v_counter


def handle_game_loop():
    while v_counter < v_fail:
        v_let = str(input("Enter a letter: "))
        if len(v_let) != 1:
            print("You should enter exactly 1 letter, try again")
            continue
        is_letter_doesnt_exist(v_let)
        is_letter_exists(v_let)
        print(v_mark)
        if check_if_win():
            break
        print(v_fail - v_counter, "failures left!\n")


def initialize_v_mark():
    for i in range(len(v_word)):
        v_mark_lst.append("-")
    return "".join(v_mark_lst)


def ask_user(message):
    global v_again
    v_again = str(input(message))
    if v_again != 'y' and v_again != 'Y':
        print('Thank you! Bye Bye')
        return False
    return True


def game_number_with_ask_user():
    if v_count_games > 1:
        if not ask_user('Play again? Y/N: '):
            return False
        return True
    else:
        if not ask_user('Ready to play? Y/N: '):
            return False
        return True


v_again = 'Y'
v_count_games = 1
v_fail = 8

while v_again == 'y' or v_again == 'Y':
    if not game_number_with_ask_user():
        break
    v_word = str(input('Enter your word:'))
    if len(v_word) < 2:
        v_word = str(input("Didn\'t enter, try again: "))
    v_mark_lst = []
    v_mark = initialize_v_mark()
    print("\n" * 18, v_mark)
    print('a word with {} letters\nYou have {} failures.'.format(len(v_word), v_fail), "\n")
    v_counter = 0
    handle_game_loop()
    check_if_fail()
