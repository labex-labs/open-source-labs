# Tik Tac Toe

To get started, open the editor. You can see the following files from your editor.

```txt
├── public
├── src
│   ├── components
│   │   ├── common
│   │   │   └── Utils.js
│   │   ├── Board.js
│   │   ├── Game.js
│   │   └── Square.js
│   ├── App.css
│   ├── App.js
│   ├── App.test.js
│   ├── index.css
│   ├── index.js
│   ├── logo.svg
│   ├── reportWebVitals.js
│   └── setupTests.js
├── package-lock.json
└── package.json
```

## Requirements

- To install the project dependencies, use the following command:

  ```bash
  npm i
  ```

- Please complete this challenge in the `src/components/Game.js` file.
- Use the `useState` hook to define three state variables: board, xTurn, and winner.
  - `board` represents the state of the game board. It is initialized as an array of 9 elements, where each element is initially set to null.
  - `xTurn` is a boolean flag indicating whether it is currently X's turn.
  - `winner` stores the result of the `calculateWinner` function, which determines the winner based on the current state of the board.
- The `handleClick` function is called when a square on the game board is clicked.
  - It creates a copy of the current board state using the spread operator (`[...board]`) and assigns it to tmpBoard.
  - If there is already a winner (winner is truthy) or the clicked square is already marked (`tmpBoard[i]` is truthy), the function returns without making any changes.
  - Otherwise, it updates the value of the clicked square in `tmpBoard` to either "X" or "O" based on the value of `xTurn`.
  - The updated `tmpBoard` is then set as the new value for the board state using `setBoard`, and xTurn is toggled using setXTurn.

## Example

Once you have completed the code, run it with the following command:

```bash
npm start
```

The finished result is as follows:

![Tic Tac Toe game demo](./assets/finished.gif)
