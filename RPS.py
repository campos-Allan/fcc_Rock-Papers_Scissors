"""first challenge from 'Machine Learning with Python'
on FreeCodeCamp.org
"""

from typing import List, Dict


def player(prev_opponent_play: str,
           opponent_history: List = [],
           play_order: List[Dict] = [{}]) -> str:
    """strategy is an cleaner version of abbey
    with kris

    Args:
        prev_opponent_play (str): last bot play
        opponent_history (List, optional): all the plays made by bot. Defaults to [].
        play_order (List[Dict], optional): last 6 plays of the bot to guess the next. 
        Defaults to [{}].

    Returns:
        str: guess the next move to beat the bot
    """

    if not prev_opponent_play:
        prev_opponent_play = 'R'
    opponent_history.append(prev_opponent_play)

    last_five = "".join(opponent_history[-5:])
    last_six = "".join(opponent_history[-6:])
    if len(last_six) == 6:
        try:
            play_order[0][last_six] += 1
        except:
            play_order[0][last_six] = 1
    else:
        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        return ideal_response[prev_opponent_play]

    potential_plays = [
        last_five + "P",
        last_five + "R",
        last_five + "S",
    ]
    try:
        sub_order = {
            k: play_order[0][k]
            for k in potential_plays if k in play_order[0]
        }

        prediction = max(sub_order, key=sub_order.get)[-1:]

        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        return ideal_response[prediction]
    except:
        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        return ideal_response[prev_opponent_play]
