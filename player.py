#Imnports

import math 
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

    #we want all players to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game): #game is the tictactoe game
        #get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        move = None
        while move not in game.available_moves():
            move = input("Ingrese su movimiento (0-8): ")
            try:
                move = int(move)
            except ValueError:
                print("Por favor ingrese un número válido (0-8).")
        return move