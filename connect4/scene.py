from .utils import clear_console
from .player import Player
from .enums import Orientation


class Scene(object):
    name = "Connet 4"
    screen = None
    level = None
    is_finished = None
    winner = None
    players = [None, None]
    state = None
    colors = ["x", "#"]

    def __init__(self) -> None:
        self.level = 1
        self.is_finished = False
        self.winner = None

        self.screen = []
        for i in range(6):
            self.screen.append([])
            for _ in range(7):
                self.screen[i].append(' ')

        clear_console()
        print(f"Welcome to {self.name}!")
        name = str(input("What is the 1st player name? "))
        self.players[0] = Player(name, self.colors[0])
        name = str(input("What is the 2nd player name? "))
        self.players[1] = Player(name, self.colors[1])

        self.state = self.players[0]

    def restart_game(self) -> None:
        self.level = 1
        self.is_finished = False
        self.winner = None
        self.state = self.players[0]
        
        self.screen = []
        for i in range(6):
            self.screen.append([])
            for _ in range(7):
                self.screen[i].append(' ')

    def next_state(self):
        if self.state == self.players[0]:
            self.state = self.players[1]
        else:
            self.state = self.players[0]
        self.level += 1

    def check_state(self):
        for i in range(6):
            for j in range(7):
                if self.screen[i][j] != ' ':
                    if self.check_state_vertical(i, j):
                        self.is_finished = True
                        return
                    
                    if self.check_state_horizontal(i, j):
                        self.is_finished = True
                        return
        
    def check_state_vertical(self, row, col):
        is_ok = False
        consecutive_count = 0
    
        for i in range(row, 6):
            if self.screen[i][col].lower() == self.screen[row][col].lower():
                consecutive_count += 1
            else:
                break
    
        if consecutive_count >= 4:
            is_ok = True
            if self.players[0].color.lower() == self.screen[row][col].lower():
                self.winner = self.players[0]
            else:
                self.winner = self.players[1]
    
        return is_ok
    
    def check_state_horizontal(self, row, col):
        is_ok = False
        consecutive_count = 0
        
        for j in range(col, 7):
            if self.screen[row][j].lower() == self.screen[row][col].lower():
                consecutive_count += 1
            else:
                break

        if consecutive_count >= 4:
            is_ok = True
            if self.players[0].color.lower() == self.screen[row][col].lower():
                self.winner = self.players[0]
            else:
                self.winner = self.players[1]

        return is_ok
    
    def find4(self):
        for i in range(6):
            for j in range(7):
                if self.screen[i][j] != ' ':
                    if self.check_state_vertical(i, j):
                        self.show4(i, j, Orientation.VERTICAL)
                    
                    if self.check_state_horizontal(i, j):
                        self.show4(i, j, Orientation.HORIZONTAL)
    
    def show4(self, row, col, direction):
        if direction == Orientation.VERTICAL:
            for i in range(4):
                self.screen[row+i][col] = self.screen[row+i][col].upper()
        
        elif direction == Orientation.HORIZONTAL:
            for i in range(4):
                self.screen[row][col+i] = self.screen[row][col+i].upper()
        
        else:
            raise Exception("Invalid direction")
    
    def print_state(self):
        clear_console()
        print("Level: " + str(self.level))

        for i in range(5, -1, -1):
            print("\t", end="")
            for j in range(7):
                print("| " + str(self.screen[i][j]), end=" ")
            print("|")
        print("\t  -   -   -   -   -   -   - ")
        print("\t  1   2   3   4   5   6   7 ")

        if self.is_finished:
            print("Game over!")
            if self.winner != None:
                print(str(self.winner.name) + " - winner!")
    
    def event_tick(self):
        player = self.state

        if self.level > 42:
            self.is_finished = True
            return

        j = player.event()

        for i in range(6):
            if self.screen[i][j] == ' ':
                self.screen[i][j] = player.color
                self.next_state()
                self.check_state()
                self.print_state()
                return
        raise Exception("Invalid state")



