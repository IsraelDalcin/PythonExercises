""" ------------------------------------------DESCRIPTION-------------------------------------------------
If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
We want our function to return:

-1 if the board is not yet finished AND no one has won yet (there are empty spots),
1 if "X" won,
2 if "O" won,
0 if it's a cat's game (i.e. a draw).
You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
----------------------------------------------------------------------------------------------------------
""" 

def is_solved(board):
    vencedor = 0
    
    # Checando linhas
    if board[0][0] == board[0][1] == board[0][2] != 0:
        vencedor = board[0][0]
    if board[1][0] == board[1][1] == board[1][2] != 0:
        vencedor = board[1][0]
    if board[2][0] == board[2][1] == board[2][2] != 0:
        vencedor = board[2][0]
        
    # Checando vencedor linhas
    if vencedor == 1:
        return vencedor
    if vencedor == 2:
        return vencedor
    
    # Checando colunas
    if board[0][0] == board[1][0] == board[2][0] != 0:
        vencedor = board[0][0]            
    if board[0][1] == board[1][1] == board[2][1] != 0:
        vencedor = board[0][1]
    if board[0][2] == board[1][2] == board[2][2] != 0:
        vencedor = board[0][2]
            
    # Checando vencedor colunas
    if vencedor == 1:
        return vencedor
    if vencedor == 2:
        return vencedor
    
    # Verificando diagonais
    if board[0][0] == board[1][1] == board[2][2] != 0:
        vencedor = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        vencedor = board[0][2]
            
    # Checando vencedor diagonais
    if vencedor == 1:
        return vencedor
    if vencedor == 2:
        return vencedor
    
    # Checando se o jogo está empatado ou unfinished
    if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        return 0
    else:
        return -1