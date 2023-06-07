import json
import random
import math
from flask import Flask, request
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*', logger=True, engineio_logger=True, debug=True)


class GameState:
    def __init__(self):
        self.grid = None
        self.player_x = None
        self.player_y = None
        self.treasure_x = None
        self.treasure_y = None

    def generate_random_grid(self):
        grids = [
            [['W', 'W', 'W', 'W', 'W'],
            ['W', 'T', 'G', 'W', 'W'],
            ['W', 'G', 'G', 'G', 'W'],
            ['W', 'G', 'W', 'G', 'W'],
            ['W', 'W', 'W', 'W', 'W']],

            [['W', 'W', 'W', 'W', 'W'],
            ['W', 'G', 'G', 'T', 'W'],
            ['W', 'W', 'G', 'W', 'W'],
            ['W', 'W', 'G', 'G', 'W'],
            ['W', 'W', 'W', 'W', 'W']],
            ]

        selected_grid = random.choice(grids)

        # Find the player and treasure positions
        self.player_x, self.player_y = None, None
        self.treasure_x, self.treasure_y = None, None
        for y in range(len(selected_grid)):
            for x in range(len(selected_grid[0])):
                if selected_grid[y][x] == 'G':
                    self.player_x, self.player_y = x, y
                elif selected_grid[y][x] == 'T':
                    self.treasure_x, self.treasure_y = x, y

        self.grid = selected_grid

# Create an instance of the GameState class
game_state = GameState()


def emit_game_state():
    if (game_state.grid != None):
        print("emitting game, state")
        game_state_json = json.dumps(get_socket_game_state(game_state))
        socketio.emit('game_state', game_state_json, broadcast=True)
    else:
        print("game not yet started. nothing to emit.")
# Endpoint for game actions
@app.route('/api/game')
def game():
    command = request.args.get('command')
    print(command)
    # command = request.json['command']

   # Process the command
    if command == 'START':
        game_state.generate_random_grid()
        print_grid(game_state.grid)  # Print the grid to the server console
        response = get_game_state(game_state)
    elif command == 'UP':
        response = move_player(game_state, game_state.player_x, game_state.player_y - 1)
    elif command == 'DOWN':
        response = move_player(game_state, game_state.player_x, game_state.player_y + 1)
    elif command == 'LEFT':
        response = move_player(game_state, game_state.player_x - 1, game_state.player_y)
    elif command == 'RIGHT':
        response = move_player(game_state, game_state.player_x + 1, game_state.player_y)
    elif command == 'PICK_UP':
        response = pick_up_treasure(game_state)
    else:
        response = {'message': 'Invalid command'}
    emit_game_state()
    return response


@socketio.on('connect')
def handle_connect():
    print('connect')
    emit_game_state()

def get_game_state(state):
    grid = state.grid
    player_x = state.player_x
    player_y = state.player_y
    treasure_x = state.treasure_x
    treasure_y = state.treasure_y
    
    # Get the current cell and adjacent cells
    current_cell = grid[player_y][player_x]
    adjacent_cells = {
        'up': state.grid[player_y - 1][player_x] if player_y > 0 else None,
        'left': grid[player_y][player_x - 1] if player_x > 0 else None,
        'down': grid[player_y + 1][player_x] if player_y < len(grid) - 1 else None,
        'right': grid[player_y][player_x + 1] if player_x < len(grid[0]) - 1 else None
    }
    
    distance = math.sqrt((player_x - treasure_x)**2 + (player_y - treasure_y)**2)
    
    return {'current_cell': current_cell, 'adjacent_cells': adjacent_cells, 'distance_to_treasure': distance}

def get_socket_game_state(state):
    state_json = get_game_state(state)
    state_json['grid'] = state.grid
    state_json['player_x'] = state.player_x
    state_json['player_y'] = state.player_y
    return state_json


def move_player(state, new_x, new_y):
    if state.grid[new_y][new_x] != 'W':
        state.player_x = new_x
        state.player_y = new_y
        response = get_game_state(state)
    else:
        response = {'message': 'Invalid move'}
    
    return response


def pick_up_treasure(state):
    if state.grid[state.player_y][state.player_x] == 'T':
        response = {'message': 'Treasure picked up!'}
    else:
        response = {'message': 'No treasure at the current location'}
    
    return response

def print_grid(grid):
    for row in grid:
        print(" ".join(row))


if __name__ == '__main__':
    game_state = GameState()
    socketio.run(app, host='0.0.0.0', port=5001)
