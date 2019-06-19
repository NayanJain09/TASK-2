class Player(object):
    def __init__(self, name, symbol, initial_score=0):
        self.name= name
        self.symbol= symbol
        self.score= initial_score

    def won_match(self):
        self.score+= 100

    def lost_match(self):
        self.score-= 50

    def show_score(self):
        print('Player {}: {} points'.format(self.name, self.score))

class PlayingField(object):
    def __init__(self):
        self.field= [
                     [None, None, None],
                     [None, None, None],
                     [None, None, None]
                    ]

    def show_field(self):
        for row in self.field:
            for player in row:
                print('_' if player is None else player.symbol,end=' ')
            print()

    def set_player(self, x, y, player):
        if self.field[y][x] is not None:
            return False

        self.field[y][x]= player

        return True

    def full_board(self):
     for row in self.field:
        for col in self.field:
            if col is '_':
                return False
            else:
             return True

    def check_won(self, x, y, player):
     if self.field[0][x] == player.symbol and self.field[1][x] == player.symbol and self.field[2][x] == player.symbol:
        return True
     elif self.field[y][0] == player.symbol and self.field[y][1] == player.symbol and self.field[y][2] == player.symbol:
        return True
     elif self.field[0][0] == player.symbol and  self.field[1][1] == player.symbol and self.field[2][2] == player.symbol:
        return True
     elif self.field[0][2] == player.symbol and  self.field[1][1] == player.symbol and  self.field[2][0] == player.symbol:
        return True
     else:
        return False


name_1= input('Name of Player 1: ')
name_2= input('Name of Player 2: ')

players= [
              Player(name_1, 'X'),
              Player(name_2, 'O')
              ]
field= PlayingField()
    
while True:
        for player in players:
            print(player.symbol)
            y= int(input('Player {} choose your row: '.format(player.name))) - 1
            x= int(input('Player {} choose your column: '.format(player.name))) - 1

            if not field.set_player(x, y, player):
                print('That field is already occupied.')
            else :
                field.show_field()
                for player in players:
                 print('{}: {}'.format(player.name, player.score))
            if field.check_won(x,y,player):  
              print('Player {} won the game.'.format(player.name))
              exit(0)

             
