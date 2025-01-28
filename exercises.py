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

        move = input(f"Enter a valid move (example: A1): ").lower()
        
        if move in {'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'} and self.board[move] == None:
        #   print(f"Previous board value: {self.board[move]}")
          self.board[move] = self.turn
        #   print(f"New board value: {self.board[move]}")
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
      


    # def play_game(self, instance):
    #   print('Welcome to Tic Tac Toe')
    #   instance.print_board()
    #   instance.print_message()
    #   instance.get_move()

           
           
           
        

    

game_instance = Game()

game_instance1 = Game()

# game_instance.play_game(game_instance1)

# game_instance.print_board()

game_instance.print_message()

game_instance.get_move()

game_instance.print_board()

game_instance.check_winner()

game_instance.get_move()

game_instance.print_board()

game_instance.check_winner()

game_instance.get_move()

game_instance.print_board()

game_instance.check_winner()





