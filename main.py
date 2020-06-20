import chess

chess_board = chess.ChessBoard()
for y in range(8):
	for x in range(8):
		chess_board.matrix[x][y] = {'exist' : False, 'name' : None, 'color' : None}

	
chess_board.matrix[4][4] = {"exist" : True, 'name' : 'q', 'color' : 'w'}
chess_board.matrix[6][4] = {"exist" : True, 'name' : 'q', 'color' : 'w'}

if chess.CheckQueenOrbit(chess_board, 4, 4, 6, 4) == 1:
	print("can move")
else: 
	print("can't move")