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
            return 1
 
    def Movepiece(self, x_orig, y_orig, x_dest, y_dest):

        if self.CheckExist(x_orig, y_orig) != 1 :
            return -1

        dest_killed_flage = False
        if self.CheckExist(x_dest, y_dest) == -1:
            return -1
        elif self.CheckExist(x_dest, y_dest) == 0:
            dest_killed_flage = False
        elif self.CheckExist(x_dest, y_dest) == 1:
            dest_killed_flage = True
        else:
            print("error")


        # piece move process
        dest_piece = self.matrix[x_dest][y_dest]
        self.matrix[x_dest][y_dest] = self.matrix[x_orig][y_orig]
        self.matrix[x_orig][y_orig] = {'exist' : False}

        if dest_piece.get('exist') == True :
            return 2
        else :
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



        
chess_board = ChessBoard()
print("CheckExist(0, 0) : ", chess_board.CheckExist(0, 0))
print( "return val: ", chess_board.Movepiece(0, 0, 4, 4))
chess_board.ShowBoard()
print( "SearchPiece(r, w)", chess_board.SearchPiece('r', 'w'))
