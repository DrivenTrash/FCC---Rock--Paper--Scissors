# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from RPS_game import abbey

def player(prev_play, opponent_history=[], i = 0):
    if i < 300:
        ##clone_abbey aufrufen
        guess = random()
    if i = 300:
        opponent = AI-Ergebnis
    if i > 300 and i < 100:
        if opponent == "abbey":
            guess = beat_abbey(args) ##fortsetzen


    return guess

def beat_quincy(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    choices = ["P", "P", "S", "S", "R"]
    
    guess = choices[len(opponent_history) % len(choices)]
    
    return guess

def beat_mrugesh(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    choices = ["R", "S", "P"]
    
    key = (len(opponent_history) - 1) // 5 % 3
    guess = choices[key]
    
    return guess

def beat_kris(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    choices = ["P", "R", "S"]
    
    key = (len(opponent_history) - 1) % 3
    guess = choices[key]
    
    return guess

def clone_abbey(prev_opponent_play,
          opponent_history=[],
          play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):

    if not prev_opponent_play:
        prev_opponent_play = 'R'
    opponent_history.append(prev_opponent_play)

    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [
        prev_opponent_play + "R",
        prev_opponent_play + "P",
        prev_opponent_play + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]

def beat_abbey(prev_play, own_history=[]): 
    own_play = {'': '', 'P': 'S', 'R': 'P', 'S': 'R'}
    result = clone_abbey(own_play[prev_play])
    guess = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    print(result)
    return guess[result]