board=[" " for i in range(9)]
def display_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+--+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+--+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()
def check_winners(player):
    winning_positions=[
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in winning_positions:
        if all(board[pos]==player for pos in combo):
            return True
    return False
def board_full():
    return " " not in board
current_player="X"
while True:
    display_board()
    position=int(input(f"Player {current_player} choose from 1 to 9 "))-1
    if position<0 or position>8:
        print("Invalid position")
        continue
    if board[position]!=" ":
        print("Space already filled")
        continue
    board[position]=current_player
    if check_winners(current_player):
        display_board()
        print(f"{current_player} won the game.")
        break
    if board_full():
        display_board()
        print("It's a draw.")
        break
    current_player='O' if current_player=='X' else 'X'