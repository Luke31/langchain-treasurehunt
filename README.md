## langchain-treasurehunt
You find yourself in a dimly lit dungeon, with your torch barely providing enough light to see your immediate surroundings. The flickering flame casts eerie shadows on the damp stone walls. Your objective is clear: find the treasure hidden within this labyrinthine maze. But beware, the limited visibility adds to the challenge as you cautiously navigate through the darkness. Will you discover the treasure before your torch fades away completely? The race against time begins.

![ui rendering](treasure-hunt-agent.gif).

## Start game

`docker compose up -d`

## Observe game in browser

http://127.0.0.1:8089/

It will just show a list of buttons, that's fine.

## Let's try and solve the game step-by-step using LangChain and OpenAI

- Hint: Copy-paste `.env.sample` to `.env` and add your OpenAPI key 

### Python

1. `cd actor`
2. `poetry install` (Using Poetry (version 1.4.2))
3. `poetry run main`

###  Jupyter

1. `poetry install` (Using Poetry (version 1.4.2))
2. `poetry run jupyter notebook`
3. Open `langchain_treasurehunt.ipynb`
4. Run cells step by step manually

## Play the game using api
For each request, the api returns the surrounding cells and current cells. It also returns the distance to the treasure:
```
"adjacent_cells": {
    "down": "G",
    "left": "W",
    "right": "W",
    "up": "T"
  },
"current_cell": "G",
"distance_to_treasure": 2.8284271247461903
```

### Start game

```
curl http://localhost:8089/api/game?command=START
{
  "adjacent_cells": {
    "down": "W",
    "left": "G",
    "right": "W",
    "up": "G"
  },
  "current_cell": "G",
  "distance_to_treasure": 2.8284271247461903
}
```

### Move up

```
curl http://localhost:8089/api/game?command=UP
{
  "adjacent_cells": {
    "down": "G",
    "left": "W",
    "right": "W",
    "up": "T"
  },
  "current_cell": "G",
  "distance_to_treasure": 1.0
}
```

### Pick up the treasure

```
curl http://localhost:8089/api/game?command=PICK_UP
{
  "message": "Treasure picked up!"
}
```

## Credits
Game-description, flask-api server, react-app and nginx config created with help from ChatGPT.