def sum(a, b, c ):
    return a + b + c

def printBoard(player1State, player2State):
    zero = 'X' if player1State[0] else ('O' if player2State[0] else 0)
    one = 'X' if player1State[1] else ('O' if player2State[1] else 1)
    two = 'X' if player1State[2] else ('O' if player2State[2] else 2)
    three = 'X' if player1State[3] else ('O' if player2State[3] else 3)
    four = 'X' if player1State[4] else ('O' if player2State[4] else 4)
    five = 'X' if player1State[5] else ('O' if player2State[5] else 5)
    six = 'X' if player1State[6] else ('O' if player2State[6] else 6)
    seven = 'X' if player1State[7] else ('O' if player2State[7] else 7)
    eight = 'X' if player1State[8] else ('O' if player2State[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")
    
def board_stat(player1State, player2State):
    zero = 'X' if player1State[0] else ('O' if player2State[0] else 0)
    one = 'X' if player1State[1] else ('O' if player2State[1] else 1)
    two = 'X' if player1State[2] else ('O' if player2State[2] else 2)
    three = 'X' if player1State[3] else ('O' if player2State[3] else 3)
    four = 'X' if player1State[4] else ('O' if player2State[4] else 4)
    five = 'X' if player1State[5] else ('O' if player2State[5] else 5)
    six = 'X' if player1State[6] else ('O' if player2State[6] else 6)
    seven = 'X' if player1State[7] else ('O' if player2State[7] else 7)
    eight = 'X' if player1State[8] else ('O' if player2State[8] else 8)
    board_status = [zero, one, two, three, four, five, six, seven, eight]
    return board_status

def checkWin(player1State, player2State):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(player1State[win[0]], player1State[win[1]], player1State[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(sum(player2State[win[0]], player2State[win[1]], player2State[win[2]]) == 3):
            print("O Won the match")
            return 0
    
    board_status = board_stat(player1State, player2State)
    
    if(board_status[0] != 0 and board_status[1] != 1 and board_status[2] != 2 and
       board_status[3] != 3 and board_status[4] != 4 and board_status[5] != 5 and
       board_status[6] != 6 and board_status[7] != 7 and board_status[8] != 8):
        print('Game ended in Draw')
        return 2
        
    return -1
    
if __name__ == "__main__":
    player1State = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    player2State = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    while(True):
        printBoard(player1State, player2State)
        board_stat(player1State, player2State)
        if(turn == 1):
            print("X's Chance")
            value = int(input("Please enter a value: "))
            player1State[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            player2State[value] = 1
        cwin = checkWin(player1State, player2State)
        if(cwin != -1):
            print("Match over")
            break
        
        turn = 1 - turn