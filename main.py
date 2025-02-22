# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player, beat_quincy, beat_mrugesh, beat_kris, beat_abbey
from unittest import main

# play(beat_quincy, quincy, 1000)
play(beat_abbey, abbey, 1000, True)
# play(beat_kris, kris, 1000)
# play(beat_mrugesh, mrugesh, 1000)

# Uncomment line below to play interactively against a bot:
# play(human, quincy, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)



# Uncomment line below to run unit tests automatically
# main(module='test_module', exit=False)