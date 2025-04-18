from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Magikarp(Water):
    def __init__(self):
        moves = [
            Move("Splash", "NORMAL", 0),
            Move("Tackle", "NORMAL", 40),
            Move("Bounce", "FLYING", 85),
            Move("Hydro Pump", "WATER", 110)
        ]
        super().__init__("Golduck", 80, moves, "./TVPoke/Pokemon/imgs/Magikarp.png")