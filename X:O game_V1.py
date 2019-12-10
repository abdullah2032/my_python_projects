## this code is  X/O game for two real players

# below is assighning the game board list to be used in printing the game board to the user & determining the game end
game_board = [1,2,3,4,5,6,7,8,9]


#turn variable is used to identify which players turn to play, game condition is used to identify if either players have won yet
turn = 1
winner_player = 0


# assigning the first and second users to X & O
player1 = input('the first player wants X or O ?')
player1 = player1.upper()

while player1 !='X' and player1 !='O':
    player1 = input('invalid, please choose either X or O')
    player1 = player1.upper()

if player1 == 'X':
    player2 = 'O'    
else:
    player2 = 'X'


# below is the print function to show the players the game board
def print_xo(s):
    print(s[0],' | ',s[1],' | ',s[2])
    print('---|-----|---')
    print(s[3],' | ',s[4],' | ',s[5])
    print('---|-----|---')
    print(s[6],' | ',s[7],' | ',s[8])


# input allocation function, used to allocate X or O (user input) on the game board
def input_allocation_func(input_allocation):
    
    s = game_board
    if input_allocation == 1 and s[0] == 1:
        s[0] = player
    elif input_allocation == 2 and s[1] == 2:
        s[1] = player
    elif input_allocation == 3 and s[2] == 3:
        s[2] = player
    elif input_allocation == 4 and s[3] == 4:
        s[3] = player
    elif input_allocation == 5 and s[4] == 5:
        s[4] = player
    elif input_allocation == 6 and s[5] == 6:
        s[5] = player
    elif input_allocation == 7 and s[6] == 7:
        s[6] = player
    elif input_allocation == 8 and s[7] == 8:
        s[7] = player
    elif input_allocation == 9 and s[8] == 9:
        s[8] = player
    return(s)


# win condition function is used to determine the winner
def win_condition(s, p1, p2):
    
    player1_win1 = s[0] == s[1] == s[2] == p1
    player1_win2 = s[3] == s[4] == s[5] == p1
    player1_win3 = s[6] == s[7] == s[8] == p1
    player1_win4 = s[0] == s[3] == s[6] == p1
    player1_win5 = s[1] == s[4] == s[7] == p1
    player1_win6 = s[2] == s[5] == s[8] == p1
    player1_win7 = s[0] == s[4] == s[8] == p1
    player1_win8 = s[2] == s[4] == s[6] == p1
    
    player2_win1 = s[0] == s[1] == s[2] == p2
    player2_win2 = s[3] == s[4] == s[5] == p2
    player2_win3 = s[6] == s[7] == s[8] == p2
    player2_win4 = s[0] == s[3] == s[6] == p2
    player2_win5 = s[1] == s[4] == s[7] == p2
    player2_win6 = s[2] == s[5] == s[8] == p2
    player2_win7 = s[0] == s[4] == s[8] == p2
    player2_win8 = s[2] == s[4] == s[6] == p2
    
    if player1_win1 or player1_win2 or player1_win3 or player1_win4 or player1_win5 or player1_win6 or player1_win7 or player1_win8:
        winner = 1                                                         # winner is used to determine the winner player
    elif player2_win1 or player2_win2 or player2_win3 or player2_win4 or player2_win5 or player2_win6 or player2_win7 or player2_win8:
        winner = 2                                                         # winner is used to determine the winner player
    else:
        winner = 0
    return winner
    
    
# while loop that ends when the game board variables is filled with either X or O
while (game_board[0] == 1 or game_board[1] == 2 or game_board[2] == 3 or game_board[3] == 4 or game_board[4] == 5 or game_board[5] == 6 or game_board[6] == 7 or game_board[7] == 8 or game_board[8] == 9) and winner_player == 0:
    print('game_board')
    print_xo(game_board)
    
    if turn%2 == 1:
        user_input = int(input('please choose a number to play'))
        player = player1
        game_board = input_allocation_func(user_input)
        
    elif turn%2 == 0:
        user_input = int(input('please choose a number to play'))
        player = player2
        game_board = input_allocation_func(user_input)
        
    winner_player = win_condition(game_board, player1, player2) 
    turn +=1
    

# the three if statements below are used to determine the game result
if winner_player == 1:
    print('the winner is player 1')
    
elif winner_player == 2:
    print('the winner is player 2')

elif winner_player == 0:
    print('DRAW, no one WON')
    
print('end of the game !!')
print_xo(game_board)