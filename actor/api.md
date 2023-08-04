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
