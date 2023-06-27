import React, { useState } from "react";
import { calculateWinner } from "./common/Utils";
import Board from "./Board";

const style = {
  container: {
    display: "flex",
    flexDirection: "column",
    alignContent: "center",
    justifyContent: "space-evenly",
    height: "100%",
  },
  info: {
    fontSize: "2rem",
    opacity: "0.5",
    textShadow: "5px 5px #424242",
  },
};

const Game = () => {
  // TODO: Complete the code here
  const handleClick = (i) => {

  };

  const resetBoard = () => (
    <button onClick={() => setBoard(Array(9).fill(null))}>Start Game</button>
  );

  return (
    <div style={style.container}>
      <p style={style.info}>
        {winner ? "Winner: " + winner : "Next Player: " + (xTurn ? "X" : "O")}
      </p>
      <Board squares={board} handleClick={handleClick} />
      <div>{resetBoard()}</div>
    </div>
  );
};

export default Game;
