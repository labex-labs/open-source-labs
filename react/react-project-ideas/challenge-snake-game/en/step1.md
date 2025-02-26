# Snake Game

To get started, open the editor. You can see the following files from your editor.

```txt
├── public
├── src
│   ├── components
│   │   ├── Food.js
│   │   └── Snake.js
│   ├── App.css
│   ├── App.js
│   ├── index.css
│   └── index.js
├── package-lock.json
└── package.json
```

## Requirements

- To install the project dependencies, use the following command:

  ```bash
  npm i
  ```

- Please complete this challenge in the `src/App.js` file.
- The `randomFoodPosition` function is defined to generate a random position for the food item on the game board.
- Inside the App function, there are several state variables defined using the useState hook:
  - `snake` represents the current state of the snake.
  - `lastDirection` represents the last direction the snake moved in.
  - `foodPosition` represents the current position of the food item.
  - `isStarted` determines if the game has started.
  - `gameOver` indicates if the game is over.
  - `playgroundRef` is a reference to the game board element.

## Example

Once you have completed the code, run it with the following command:

```bash
npm start
```

The finished result is as follows:

![Snake game final result](../assets/finished.gif)
