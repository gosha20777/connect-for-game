class Player(object):
    name = None
    color = None
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
    
    def event(self) -> int:
        print(f"Player {self.name} - {self.color}")
        column = None
        while column == None:
            try:
                number = int(input("Enter the column number): ")) - 1
                if 0 <= number <= 6:
                    column = number
                else:
                    raise ValueError()
            except ValueError:
                print("Invalid number, try again")
        return column