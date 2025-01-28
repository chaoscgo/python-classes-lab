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

    def play_game(self, instance):
        print('Welcome to Tic Tac Toe')
        instance.print_board()
        instance.print_message()

        move = input(f"Enter a valid move (example: A1): ").lower()
          if move is in [a1, a2, a3, b1, b2, b3, c1, c2, c3]:
        

    

game_instance = Game()

game_instance1 = Game()

game_instance.play_game(game_instance1)


