from PlayerClass import Player

Player1 = Player(name='Debi', attack=2, defense=2, agility=2, brutality=2, extraLife=2)
Player1.RegisterPlayer()

Player2 = Player(name='Loyd', attack=2, defense=2, agility=2, brutality=2, extraLife=2)
Player2.RegisterPlayer()

Player1.Turn(Player2)
