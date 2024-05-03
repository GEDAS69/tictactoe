import json

def save_game_state(filename, current_player, board):
    try:
        data = {
            "current_player": current_player,
            "board": board
        }
        with open(filename, 'w') as f:
            json.dump(data, f)
        print("Game state saved successfully.")
    except Exception as e:
        print("Error saving game state:", e)

def load_game_state(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            current_player = data["current_player"]
            board = data["board"]
            return current_player, board
    except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
        print("Error loading game state:", e)
        return None, None

def save_scores(filename, x_score, o_score):
    try:
        data = {
            "x_score": x_score,
            "o_score": o_score
        }
        with open(filename, 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print("Error saving scores:", e)

def load_scores(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            x_score = data["x_score"]
            o_score = data["o_score"]
            return x_score, o_score
    except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
        print("Error loading scores:", e)
        return None, None
