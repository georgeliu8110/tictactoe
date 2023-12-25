board = [
[' ', ' ', ' '],
[' ', ' ', ' '],
[' ', ' ', ' '],
]

winner = ''

def print_board():
  global board
  first_line = board[2]
  second_line = board[1]
  third_line = board[0]
  print(third_line)
  print(second_line)
  print(first_line)

def player_input(player_choice_xo):
  global board
  player_position = input("please enter your position (1 - 9): ")
  if int(player_position) in [1,2,3]:
    if board[2][int(player_position)-1] == " ":
      board[2][int(player_position)-1] = player_choice_xo
    else:
      print('invalid position, please try again!')
      player_input(player_choice_xo)
  elif int(player_position) in [4,5,6]:
    if board[1][int(player_position)-4] == " ":
      board[1][int(player_position)-4] = player_choice_xo
    else:
      print('invalid position, please try again!')
      player_input(player_choice_xo)
  elif int(player_position) in [7,8,9]:
    if board[0][int(player_position)-7] == " ":
      board[0][int(player_position)-7] = player_choice_xo
    else:
      print('invalid position, please try again!')
      player_input(player_choice_xo)
  else:
    print('invalid input, please try again!')


def horizontal_win(board):
  global winner
  for i in range(len(board)):
    if board[i][0] == "x" and board[i][0] == board[i][1] == board[i][2]:
      winner = 'x'
      return True
    elif board[i][0] == "o" and board[i][0] == board[i][1] == board[i][2]:
      winner = 'o'
      return True
  return False

def vertical_win(board):
  global winner
  for i in range(len(board)):
    if board[0][i] == "x" and board[0][i] == board[1][i] == board[2][i]:
      winner = 'x'
      return True
    elif board[0][i] == "o" and board[0][i] == board[1][i] == board[2][i]:
      winner = 'o'
      return True
  return False

def diagonal_win(board):
  global winner
  if board[0][0] == "x" and board[0][0] == board[1][1] == board[2][2]:
    winner = 'x'
    return True
  elif board[0][0] == "o" and board[0][0] == board[1][1] == board[2][2]:
    winner = 'o'
    return True
  elif board[0][2] == "x" and board[0][2] == board[1][1] == board[2][0]:
    winner = 'x'
    return True
  elif board[0][2] == "o" and board[0][2] == board[1][1] == board[2][0]:
    winner = 'o'
    return True
  return False

def game_over(board):
  if horizontal_win(board) or vertical_win(board) or diagonal_win(board):
    return True
  else:
    for i in range(len(board)):
      for j in range(len(board[i])):
        if board[i][j] == " ":
          return False
    return True

def replay():
  play_again = input('Do you want to play again? (Yes or No)')
  if play_again.lower() == 'yes':
    game_play()
  else:
    return

def game_play():

  global board

  print('Welcome to Tic Tac Toe!!')

  player1_choice_xo = ''
  player2_choice_xo = ''
  while player1_choice_xo.lower() != 'x' and player1_choice_xo.lower() != 'o':
    player1_choice_xo = input('Do you want to be X or O?')

  if player1_choice_xo.lower() == 'x':
    print('Player 1 will go first!')
    player1_choice_xo = player1_choice_xo.lower()
    player2_choice_xo = 'o'
  else:
    print('Player2 will go first!')
    player2_choice_xo = 'x'
    player1_choice_xo = 'o'

  ready_to_play = input('Are you ready to play? Enter yes or No.')

  if ready_to_play.lower() == 'yes':
    print_board()
    while True:
      if not game_over(board):
        player_input(player1_choice_xo)
        print_board()
      if not game_over(board):
        player_input(player2_choice_xo)
        print_board()
      if game_over(board):
        board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        ]
        if winner != "":
          print(f'congrats! {winner} has won the game!')
          replay()
        else:
          print('Game over with no winners!')
          replay()
  else:
    return

game_play()



