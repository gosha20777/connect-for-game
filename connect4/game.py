from .scene import Scene


class Game(object):
    scene = None
    player1 = None
    player2 = None
    is_end = None

    def __init__(self) -> None:
        self.scene = Scene()
        self.player1 = self.scene.players[0]
        self.player2 = self.scene.players[1]
        self.is_end = False
    
    def run(self):
        self.scene.print_state()
        while not self.is_end:
            while not self.scene.is_finished:
                self.scene.event_tick()
            self.scene.find4()
            self.scene.print_state()

            while True:
                play_again = str(input("Would you like to play again? [y/n] "))

                if play_again.lower() == 'y': 
                    self.scene.restart_game()
                    self.scene.print_state()
                    break
                elif play_again.lower() == 'n':
                    self.is_end = True
                    break
                else:
                    print("Yes or no? [y/n] ")