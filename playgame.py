""" playgame.py

Contains the Connect 3 game playing application.
This file forms part of the assessment for CP2410 Assignment 2

************** ENTER YOUR NAME HERE ****************************

"""
from connect3board import Connect3Board
from gametree import GameTree


def main():
    print('Welcome to Connect 3 by YOUR NAME HERE')
    mode = get_mode()
    while mode != 'Q':
        if mode == 'A':
            run_two_player_mode()
        elif mode == 'B':
            run_ai_mode()
        mode = get_mode()


def run_two_player_mode():

    rows = get_int("How many rows? (3 to 7) ")
    columns = get_int("How many columns? (3 to 7) ")
    board = Connect3Board(rows,columns)

    while board.get_winner() == None:
        print(board)
        column_choice = get_int("Player {}'s turn. Choose column ({} to {}):".format(board.get_whose_turn(), 0, board.get_columns() - 1))
        if board.can_add_token_to_column(column_choice):
            board.add_token(column_choice)
        else:
            print("You cannot add a token at column {}".format(column_choice))

    print(board)

    # Display the winner if its not a draw
    if board.get_winner() != board.DRAW:
        print("Player {} wins!".format(board.get_winner()))
    else:
        print(board.get_winner())


def run_ai_mode():
    board = Connect3Board(3, 3)
    game_tree = GameTree(board)



def get_mode():
    mode = input("A. Two-player mode\nB. Play against AI\nQ. Quit\n>>> ")
    while mode[0].upper() not in 'ABQ':
        mode = input("A. Two-player mode\nB. Play against AI\nQ. Quit\n>>> ")
    return mode[0].upper()


def get_int(prompt):
    result = 0
    finished = False
    while not finished:
        try:
            result = int(input(prompt))
            finished = True
        except ValueError:
            print("Please enter a valid integer.")
    return result


if __name__ == '__main__':
    main()
