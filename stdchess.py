from board import Board
from agents import GenericAgent

board = Board()
testAgent = GenericAgent(board, 'w')

print(board.field)
print('\n\n')
print(testAgent.check_moves(3,3))