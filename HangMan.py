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
v_again = 'Y'
v_count_games = 1
v_fail = 8
while v_again == 'y' or v_again == 'Y':
    if v_count_games > 1:
        v_again = str(input('Play again? Y/N: '))
        if v_again != 'y' and v_again != 'Y':
            print('Thank you! Bye Bye')
            break
    else:
        v_again = str(input('Ready to play? Y/N: '))
        if v_again != 'y' and v_again != 'Y':
            print('Thank you! Bye Bye')
            break
    v_word = str(input('Enter your word:'))
    if len(v_word) < 2:
        v_word = str(input("Didn\'t enter, try again: "))
    v_mark = len(v_word) * '-'
    print("\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", v_mark)
    v_mark_lst = []
    for i in v_mark:
        v_mark_lst.append(i)
    print('a word with {} letters\nYou have {} failures.'.format(len(v_word), v_fail), "\n")
    v_counter = 0
    while v_counter < v_fail:
        v_let = str(input("Enter a letter: "))
        if len(v_let) != 1:
            print("You should enter exactly 1 letter, try again")
            continue
        if v_let not in v_word:
            print('There is no "'"{}"'" in the word.'.format(v_let))
            print(v_hangman[v_counter])
            v_counter += 1
        for i in range(len(v_word)):
            if v_word[i] == v_let:
                v_mark_lst[i] = v_let
                v_mark = ''
                for j in v_mark_lst:
                    v_mark += j
        print(v_mark)
        if '-' not in v_mark_lst:
            v_count_games += 1
            print("NOICE! You did it with {} failures.\n".format(v_counter))
            break
        print(v_fail - v_counter, "failures left!\n")
    if '-' in v_mark_lst:
        v_count_games += 1
        print("HAHAHIHI! You didn't do it and the man is hanged and dead!!!\n")
        print("The word is: {}".format(v_word))