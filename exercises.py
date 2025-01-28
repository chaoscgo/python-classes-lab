class Game():

    board = {
     'a1': None, 'b1': None, 'c1': None,
     'a2': None, 'b2': None, 'c2': None,
     'a3': None, 'b3': None, 'c3': None,
    }

    def __init__(self, turn='X', tie = False, winner = 'None'):
      self.turn = turn
      self.tie = tie
      self.winner = winner

    def print_board(self):
      b = self.board
      print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
      """)

    def print_message(self):
      if self.tie:
        print("Tie Game!")
      elif self.winner != 'None':
        print(f"{self.winner} wins the game!")
      else:
        print(f"It's player {self.turn}'s turn!")


    def get_move(self):
        
      while True:

        move = input(f"Player {self.turn}, enter a valid move (example: A1): ").lower()
        
        if move in {'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'} and self.board[move] == None:
          self.board[move] = self.turn
          break

        else:
           print('That is an invalid input, try again!')
      

    def check_winner(self):
      if self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1']):
        self.winner = self.turn
        print(f"{self.winner} is the winner!")
      elif self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2']):
        self.winner = self.turn
        print(f"{self.winner} is the winner!")
      elif self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3']):
        self.winner = self.turn
        print(f"{self.winner} is the winner!")
      elif self.board['a1'] and (self.board['a1'] == self.board['a2'] == self.board['a3']):
        self.winner = self.turn
        print(f"{self.winner} is the winner!")
      elif self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3']):
        self.winner = self.turn
        print(f"{self.winner} is the winner!")
      elif self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3']):
        self.winner = self.turn
        print(f"{self.winner} is the winner!")
      elif self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3']):
        self.winner = self.turn
        print(f"{self.winner} is the winner!")
      elif self.board['c1'] and (self.board['c1'] == self.board['b2'] == self.board['a3']):
        self.winner = self.turn
        print(f"{self.winner} is the winner!")
      else:
        print('No winner yet!')

    def check_tie(self):
      filled = 0

      for val in self.board.values():
        if val != None:
          filled += 1

      if filled == 9 and self.winner == 'None':
          self.tie = True
          print('Game has ended in a tie.')
          
    def switch_turn(self):
      if self.turn == 'X':
        self.turn = 'O'
      else:
        self.turn = 'X'

    def play_game(self):
      
      print('Welcome to Tic Tac Toe, want to play?')

      while self.winner == 'None' and self.tie == False:
        self.print_board()
        self.print_message()
        self.get_move()
        self.check_winner()
        self.check_tie()
        self.switch_turn()

      print('Game over, do you want to play again?')

    

game_instance = Game()

game_instance.play_game()



