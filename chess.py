import pdb


class ChessBoard:
	def __init__(self):
		self.matrix = [[0 for y in range(8)] for x in range (8)]
		self.matrix[0][1] = {'exist' : True, 'name' : 'p', 'color' : 'w'}
		self.matrix[1][1] = {'exist' : True, 'name' : 'p', 'color' : 'w'}
		self.matrix[2][1] = {'exist' : True, 'name' : 'p', 'color' : 'w'}
		self.matrix[3][1] = {'exist' : True, 'name' : 'p', 'color' : 'w'}
		self.matrix[4][1] = {'exist' : True, 'name' : 'p', 'color' : 'w'}
		self.matrix[5][1] = {'exist' : True, 'name' : 'p', 'color' : 'w'}
		self.matrix[6][1] = {'exist' : True, 'name' : 'p', 'color' : 'w'}
		self.matrix[7][1] = {'exist' : True, 'name' : 'p', 'color' : 'w'}

		self.matrix[0][0] = {'exist' : True, 'name' : 'r', 'color' : 'w'}
		self.matrix[1][0] = {'exist' : True, 'name' : 'n', 'color' : 'w'}
		self.matrix[2][0] = {'exist' : True, 'name' : 'b', 'color' : 'w'}
		self.matrix[3][0] = {'exist' : True, 'name' : 'q', 'color' : 'w'}
		self.matrix[4][0] = {'exist' : True, 'name' : 'k', 'color' : 'w'}
		self.matrix[5][0] = {'exist' : True, 'name' : 'b', 'color' : 'w'}
		self.matrix[6][0] = {'exist' : True, 'name' : 'n', 'color' : 'w'}
		self.matrix[7][0] = {'exist' : True, 'name' : 'r', 'color' : 'w'}

		self.matrix[0][6] = {'exist' : True, 'name' : 'p', 'color' : 'b'}
		self.matrix[1][6] = {'exist' : True, 'name' : 'p', 'color' : 'b'}
		self.matrix[2][6] = {'exist' : True, 'name' : 'p', 'color' : 'b'}
		self.matrix[3][6] = {'exist' : True, 'name' : 'p', 'color' : 'b'}
		self.matrix[4][6] = {'exist' : True, 'name' : 'p', 'color' : 'b'}
		self.matrix[5][6] = {'exist' : True, 'name' : 'p', 'color' : 'b'}
		self.matrix[6][6] = {'exist' : True, 'name' : 'p', 'color' : 'b'}
		self.matrix[7][6] = {'exist' : True, 'name' : 'p', 'color' : 'b'}

		self.matrix[0][7] = {'exist' : True, 'name' : 'r', 'color' : 'b'}
		self.matrix[1][7] = {'exist' : True, 'name' : 'n', 'color' : 'b'}
		self.matrix[2][7] = {'exist' : True, 'name' : 'b', 'color' : 'b'}
		self.matrix[3][7] = {'exist' : True, 'name' : 'k', 'color' : 'b'}
		self.matrix[4][7] = {'exist' : True, 'name' : 'q', 'color' : 'b'}
		self.matrix[5][7] = {'exist' : True, 'name' : 'b', 'color' : 'b'}
		self.matrix[6][7] = {'exist' : True, 'name' : 'n', 'color' : 'b'}
		self.matrix[7][7] = {'exist' : True, 'name' : 'r', 'color' : 'b'}

		for y in range(2, 6):
			for x in range(0, 8):
				self.matrix[x][y] = {'exist ': False}

	def ShowBoard(self):
		for y in range(8):
			for x in range(8):
				if self.matrix[x][7 - y].get('exist') :
					print(' ', self.matrix[x][7 - y]['name'], ' ', end = '')
				else:
					print(' ', '*', ' ', end = '')
			print('')

	#not exist 0
	#exist 1
	#if input pos value is out of range -1
	def CheckExist(self, x_pos, y_pos):
		if  ( ( (0 <= x_pos) and (x_pos <= 7)) and ( (0 <= y_pos) and (y_pos <= 7)) ) == False:
			return -1
		elif self.matrix[x_pos][y_pos].get('exist') == False: 
			return 0
		else:
			return -1

	def ReturnColor(self, x_pos, y_pos):
		if self.CheckExist(x_pos, y_pos) != 0 :
			return -1
		else :
			return self.matrix[x_pos][y_pos].get('color')

 
	def Movepiece(self, x_orig, y_orig, x_dest, y_dest):

		if self.CheckExist(x_orig, y_orig) != 1 :
			return -1
		if self.CheckExist(x_dest, y_dest) == -1:
			return -1
			
		dest_exist_flage = False
		if self.CheckExist(x_dest, y_dest) == 0:
			dest_exist_flage = False
		elif self.CheckExist(x_dest, y_dest) == 1	:
			dest_exist_flage = True
		else:
			return -1 
		# piece move process
		dest_piece = self.matrix[x_dest][y_dest]
		self.matrix[x_dest][y_dest] = self.matrix[x_orig][y_orig]
		self.matrix[x_orig][y_orig] = {'exist' : False}
		self.matrix[x_orig][y_orig] = {'name' : None}
		self.matrix[x_orig][y_orig] = {'color' : None}

		return 0
			
	def SearchPiece(self, search_piece, search_color):
		search_piece_pos = list()
		for y in range(8):
			for x in range(8):
				if ((self.matrix[x][y].get('name') == search_piece) and (self.matrix[x][y].get('color') == search_color)) == True:
					search_piece_pos.append([x, y])

		if len(search_piece_pos) == 0:
			return 0 
		elif len(search_piece_pos) >= 1:
			return search_piece_pos
		else:
			print("error")
			return -1

	#dosen't satisfy 1
	#satisfy 0
def CheckEssential(board, x_orig, y_orig, x_dest, y_dest):
	if x_orig == x_dest and y_orig == y_dest:
		print("orig pos == dest_pos")
		return -1
	elif board.CheckExist(x_orig, y_orig) != 1:
		return -1
	elif (board.CheckExist(x_dest, y_dest) == True) and (board.ReturnColor(x_dest, y_dest) == board.ReturnColor(x_orig, y_orig)):
		return -1
	else:
		return 0


def CheckKingOrbit(board, x_orig, y_orig, x_dest, y_dest):
	if CheckEssential(board, x_orig, y_orig, x_dest, y_dest) != 0:
		return -1


	if abs(x_orig - x_dest) == 1 and abs(y_orig - y_dest) == 1:
		return 1
	else:
		return -1

def CheckQueenOrbit(board, x_orig, y_orig, x_dest, y_dest):
	if CheckEssential(board, x_orig, y_orig, x_dest, y_dest) != 0:
		return -1

	if x_orig == x_dest:
		if y_dest > y_orig:
			for y in range(y_orig + 1, y_dest):
				if board.CheckExist(x_orig, y) != 0:
					return 0	
		if y_dest < y_orig:
			for y in range(y_dest + 1, y_orig):
				if board.CheckExist(x_orig, y) != 0:
					return 0	
		return 1
	elif y_orig == y_dest:
		if x_dest > x_orig:
			for x in range(x_orig + 1, x_dest - 1):
				if board.CheckExist(x, y_orig) != 0:
					return 0	
		if x_dest < x_orig:
			for x in range(x_dest + 1, x_orig- 1):
				if board.CheckExist(x, y_orig) != 0:
					return 0	
		return 1

	elif abs(x_orig - x_dest) == abs(y_orig - y_dest):
		x_variance = int(abs(x_dest - x_orig) / (x_dest - x_orig))
		y_variance = int(abs(y_dest - y_orig) / (y_dest - y_orig))
		for i in range(1, abs(x_dest - x_orig)):
			if board.CheckExist(x_orig + x_variance * i , y_orig + y_variance * i) != 0:
				return 0
		return 1
	else:
		return -1 
	
def CheckRookOrbit(board, x_orig, y_orig, x_dest, y_dest):
	if CheckEssential(board, x_orig, y_orig, x_dest, y_dest) != 0:
		return -1
	
	if x_orig == x_dest:
		if y_dest > y_orig:
			for y in range(y_orig + 1, y_dest):
				if board.CheckExist(x_orig, y) != 0:
					return 0	
		if y_dest < y_orig:
			for y in range(y_dest + 1, y_orig):
				if board.CheckExist(x_orig, y) != 0:
					return 0	
		return 1
	else:
		return -1 

	
def CheckBishopOrbit(board, x_orig, y_orig, x_dest, y_dest):
	if CheckEssential(board, x_orig, y_orig, x_dest, y_dest) != 0:
		return -1

	if abs(x_orig - x_dest) == abs(y_orig - y_dest):
		x_variance = int(abs(x_dest - x_orig) / (x_dest - x_orig))
		y_variance = int(abs(y_dest - y_orig) / (y_dest - y_orig))
		for i in range(1, abs(x_dest - x_orig)):
			if board.CheckExist(x_orig + x_variance * i , y_orig + y_variance * i) != 0:
				return 0
		return 1
	else:
		return -1 
	
def CheckPoneOrbit(board, x_orig, y_orig, x_dest, y_dest):
	if CheckEssential(board, x_orig, y_orig, x_dest, y_dest) != 0:
		return -1

	if board.ReturnColor(x_orig, y_orig) == 'w':
		if y_dest - y_orig != 1:
			return 0
		elif x_orig == x_dest:
			return 1
		elif abs(x_orig - x_dest) == 1:
			if board.CheckExist(x_dest, y_dest) == True and board.ReturnColor == 'b':
				return 0
			else:
				return 1
		else:
			return 0

	if board.ReturnColor(x_orig, y_orig) == 'b':
		if y_dest - y_orig != -1:
			return 0
		elif x_orig == x_dest:
			return 1
		elif abs(x_orig - x_dest) == 1:
			if board.CheckExist(x_dest, y_dest) == True and board.ReturnColor == 'w':
				return 1
		else:
			return 0 
			
def CheckNightOrbit(board, x_orig, y_orig, x_dest, y_dest):
	if CheckEssential(board, x_orig, y_orig, x_dest, y_dest) != 0:
		return -1
	
	if (abs(x_dest - x_orig) == 1 and abs(y_dest - y_orig) == 2) or (abs(x_dest - x_orig) == 2 and abs(y_dest - y_orig) == 1) == True:
		return 0
	else:
		return -1
	
def CheckKingSafe(board, king_color):
	king_pos = board.ReturnPos('k', king_color)
	if king_pos == 0:
		return -1
	
	king_safe_flage = True
	for y in range(8):
		for x in range(8):
			if board.CheckExist(x, y) == 1:
				if board.ReturnColor != king_color:
					if board.matrix[x][y].get('name') == 'k':
						if CheckKingOrbit(board, x, y, king_pos[0], king_pos[1]) == 1:
							king_safe_flage = False
					if board.matrix[x][y].get('name') == 'q':
						if CheckQueenOrbit(board, x, y, king_pos[0], king_pos[1]) == 1:
							king_safe_flage = False
					if board.matrix[x][y].get('name') == 'r':
						if CheckRookOrbit(board, x, y, king_pos[0], king_pos[1]) == 1:
							king_safe_flage = False
					if board.matrix[x][y].get('name') == 'b':
						if CheckBishopOrbit(board, x, y, king_pos[0], king_pos[1]) == 1:
							king_safe_flage = False
					if board.matrix[x][y].get('name') == 'n':
						if CheckNightOrbit(board, x, y, king_pos[0], king_pos[1]) == 1:
							king_safe_flage = False
					if board.matrix[x][y].get('name') == 'p':
						if CheckPoneOrbit(board, x, y, king_pos[0], king_pos[1]) == 1:
							king_safe_flage = False

	if king_safe_flage == False:
		return -1
	else:
		return 0
	


if __name__ == "__main__":         
	chess_board = ChessBoard()
	print("CheckExist(0, 0) : ", chess_board.CheckExist(0, 0))
	print( "return val: ", chess_board.Movepiece(0, 0, 4, 4))
	chess_board.ShowBoard()
	print( "SearchPiece(r, w)", chess_board.SearchPiece('r', 'w'))