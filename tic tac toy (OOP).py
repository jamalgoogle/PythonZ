class Player:
   def __init__(self):
      self.name = ""
      self.symbol = ""

   def choose_name(self):
      while True:
         name = input("Enter your name: ")
         if name.isalpha():
            self.name = name
            break
         print("Invalid name. Please enter a valid name.")

   def choose_symbol(self):
      while True:
         symbol = input(f"{self.name} Choose your symbol only(X or O): ").upper()
         if symbol in ['X', 'O']:
            self.symbol = symbol
            break
         else:
            print("Invalid symbol. Please choose X or O.")
            

class Menu:
   def start_game(self):
      menu ="""
         welcome to tic toy gameplay
         1-toStart or 2-toEnd
         Enter your choice (1 or 2) : 
      """
      choice = input(menu)
      return choice


class Board:
   def __init__(self):
      self.board = [str(i) for i in range(1 , 10)]

   def display_board(self):
      for i in range(0, 9 , 3):
         print("|".join(self.board[i:i+3]))
         if (i < 6):
            print("----------------")

   def update_board(self , chioce , symbol):
      if self.is_valid(chioce):
         self.board[chioce - 1] = symbol
         return True
      return False
   
   def is_valid(self , choice):
      return self.board[choice - 1].isdigit()

   def reset_board(self):
      self.board = [str(i) for i in range(1 , 10)]

   def check_winner(self, symbol):
      # Check rows
      for i in range(0, 9, 3):
         if self.board[i] == self.board[i+1] == self.board[i+2] == symbol: # Check rows
            return True
      # Check columns
      for i in range(3):
         if self.board[i] == self.board[i+3] == self.board[i+6] == symbol: # Check columns
            return True
      # Check diagonals
      if self.board[0] == self.board[4] == self.board[8] == symbol: # Top-left to bottom-right diagonal
         return True
      if self.board[2] == self.board[4] == self.board[6] == symbol: # Top-right to bottom-left diagonal
         return True
      return False

   def is_board_full(self):
      return all(not cell.isdigit() for cell in self.board)


class Game:
   def __init__(self):
      self.players = [Player() , Player()]
      self.board = Board()
      self.menu = Menu()
      self.current_player = 0

   def start(self):
      choice = self.menu.start_game()
      if choice == '1':
         self.setup_players()
         self.play_game()
      else:
         self.quit_game()
   
   def setup_players(self):
      for i, player in enumerate(self.players):
         player.choose_name()
         player.choose_symbol()
         if i == 0:
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
   
   def play_game(self):
      import os
      while True:
         self.board.display_board()
         current = self.players[self.current_player]
 
         choice = int(input(f"{current.name}'s turn. Choose a position (1-9): "))
         if self.board.update_board(choice, current.symbol):
            if self.board.check_winner(current.symbol):
               os.system('cls' if os.name == 'nt' else 'clear')
               self.board.display_board()
               print(f"Congratulations! {current.name} wins!")
               break
            elif self.board.is_board_full():
               os.system('cls' if os.name == 'nt' else 'clear')
               self.board.display_board()
               print("It's a draw!")
               break
            self.current_player = (self.current_player + 1) % 2
            os.system('cls' if os.name == 'nt' else 'clear')
         else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid move. Try again.")

   def quit_game(self):
      print("Thanks for playing!")
      exit()

game = Game()
game.start()
