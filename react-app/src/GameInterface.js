import React, { useState, useEffect } from 'react';
import { Button, Grid, Table, TableBody, TableCell, TableContainer, TableRow } from '@material-ui/core';
import io from 'socket.io-client';

const socket = io.connect('ws://127.0.0.1:8089');

const GameInterface = () => {
  const [gameState, setGameState] = useState(null);

  useEffect(() => {
    socket.on('game_state', handleGameState);
    return () => {
        socket.off('game_state', handleGameState);
      };
  }, []);

  const handleGameState = (gameState) => {
    console.log("gamestate:" + gameState)
    setGameState(JSON.parse(gameState));
  };

  const sendCommand = (command) => {
    fetch(`/api/game?command=${command}`, {
      method: 'GET',
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  const renderGrid = () => {
    if (!gameState) {
      return null;
    }

    const { grid, player_x, player_y } = gameState;

    return (
      <TableContainer>
        <Table>
          <TableBody>
            {grid.map((row, rowIndex) => (
              <TableRow key={rowIndex}>
                {row.map((cell, colIndex) => (
                  <TableCell key={colIndex} style={{ backgroundColor: rowIndex === player_y && colIndex === player_x ? 'yellow' : 'transparent' }}>
                    {cell}
                  </TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    );
  };

  return (
    <Grid container direction="column" alignItems="center" spacing={2}>
      <Grid item>{renderGrid()}</Grid>
      <Grid item container spacing={2} justify="center">
        <Grid item>
          <Button variant="contained" onClick={() => sendCommand('START')}>
            Start
          </Button>
        </Grid>
        <Grid item>
          <Button variant="contained" onClick={() => sendCommand('UP')}>
            Up
          </Button>
        </Grid>
        <Grid item>
          <Button variant="contained" onClick={() => sendCommand('DOWN')}>
            Down
          </Button>
        </Grid>
        <Grid item>
          <Button variant="contained" onClick={() => sendCommand('LEFT')}>
            Left
          </Button>
        </Grid>
        <Grid item>
          <Button variant="contained" onClick={() => sendCommand('RIGHT')}>
            Right
          </Button>
        </Grid>
        <Grid item>
          <Button variant="contained" onClick={() => sendCommand('PICK_UP')}>
            Pick Up
          </Button>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default GameInterface;
