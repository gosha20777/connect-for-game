import os


def clear_console() -> None:
    os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
