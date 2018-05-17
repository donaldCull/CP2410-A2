""" gametree.py

Contains the definition of the GameTree class.
This file forms part of the assessment for CP2410 Assignment 2

************** Donald Cull ****************************

"""
from connect3board import Connect3Board


class GameTree:
    MAX_PLAYER = 'O'
    MIN_PLAYER = '#'
    MAX_WIN_SCORE = 1
    MIN_WIN_SCORE = -1
    DRAW_SCORE = 0

    # noinspection PyProtectedMember
    class _Node:
        POSSIBLE_SELECTIONS = 3
        __slots__ = '_gameboard', '_children', '_score'


        def __init__(self, gameboard: Connect3Board):
            self._gameboard = gameboard
            self._children = [None] * self._gameboard.get_columns()

            if self._gameboard.get_winner() is None:
                self._create_children()
                self._compute_score()

            elif self._gameboard.get_winner() == gameboard.DRAW:
                self._score = GameTree.DRAW_SCORE

            elif self._gameboard.get_winner() == GameTree.MAX_PLAYER:
                self._score = GameTree.MAX_WIN_SCORE

            elif self._gameboard.get_winner() == GameTree.MIN_PLAYER:
                self._score = GameTree.MIN_WIN_SCORE



        def _create_children(self):

            for choice in range(self.POSSIBLE_SELECTIONS):
                # if ai can add a token create a new board and recurse
                if self._gameboard.can_add_token_to_column(choice):
                    child_board = self._gameboard.make_copy()
                    child_board.add_token(choice)
                    self._children[choice] = GameTree._Node(child_board)
                else:
                    # if no tokens can be added child is not useful
                    self._children[choice] = None




        def _compute_score(self):
            if self._gameboard.get_whose_turn() == GameTree.MAX_PLAYER:
                max_score = -2
                for child in self._children:
                    if child is not None and child._score > max_score:
                        max_score = child._score
                self._score = max_score
            else:
                min_score = 2
                for child in self._children:
                    if child is not None and child._score < min_score:
                        min_score = child._score
                self._score = min_score



    class _Position:
        def __init__(self, node):
            self._node = node

        def get_gameboard(self):
            """ Return the node's gameboard """
            return self._node._gameboard

        def get_child(self, column):
            """ Return a Position object for the column-th child of the node """
            return GameTree._Position(self._node._children[column])

        def get_children_scores(self):
            """ Return a list of the scores for all child nodes """
            return [child._score if child is not None else None for child in self._node._children]

    def __init__(self, root_board):
        self._root = GameTree._Node(root_board)

    def get_root_position(self):
        """ Return a Position object at the root of the game tree """
        return GameTree._Position(self._root)