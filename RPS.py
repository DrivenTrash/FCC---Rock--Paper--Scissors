# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from RPS_game import abbey

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

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

def beat_abbey(prev_play, opponent_history=[]): 
    own_play = {'': '', 'P': 'S', 'R': 'P', 'S': 'R'}
    result = abbey(own_play[prev_play])
    guess = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    print(result)
    return guess[result]