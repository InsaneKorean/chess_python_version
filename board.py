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

        self.matrix[0][6] = {'exist' : True, 'name' : 'p', 'color' : 'w'}
        self.matrix[1][6] = {'exist' : True, 'name' : 'p', 'color' : 'w'}
        self.matrix[2][6] = {'exist' : True, 'name' : 'p', 'color' : 'w'}
        self.matrix[3][6] = {'exist' : True, 'name' : 'p', 'color' : 'w'}
        self.matrix[4][6] = {'exist' : True, 'name' : 'p', 'color' : 'w'}
        self.matrix[5][6] = {'exist' : True, 'name' : 'p', 'color' : 'w'}
        self.matrix[6][6] = {'exist' : True, 'name' : 'p', 'color' : 'w'}
        self.matrix[7][6] = {'exist' : True, 'name' : 'p', 'color' : 'w'}

        self.matrix[0][7] = {'exist' : True, 'name' : 'r', 'color' : 'w'}
        self.matrix[1][7] = {'exist' : True, 'name' : 'n', 'color' : 'w'}
        self.matrix[2][7] = {'exist' : True, 'name' : 'b', 'color' : 'w'}
        self.matrix[3][7] = {'exist' : True, 'name' : 'k', 'color' : 'w'}
        self.matrix[4][7] = {'exist' : True, 'name' : 'q', 'color' : 'w'}
        self.matrix[5][7] = {'exist' : True, 'name' : 'b', 'color' : 'w'}
        self.matrix[6][7] = {'exist' : True, 'name' : 'n', 'color' : 'w'}
        self.matrix[7][7] = {'exist' : True, 'name' : 'r', 'color' : 'w'}

        for y in range(2, 6):
            for x in range(0, 8):
                self.matrix[x][y] = {'exist ': False}


    def ShowBoard(self):
        for y in range(8):
            for x in range(8):
                if self.matrix[x][y].get('exist') :
                    print(' ', self.matrix[x][y]['name'], ' ', end = '')
                else:
                    print(' ', '*', ' ', end = '')
            print('')

chess_board = ChessBoard()
chess_board.ShowBoard()
