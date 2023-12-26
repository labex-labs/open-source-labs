# Stopwatch

To get started, open the editor. You can see the following files from your editor.

```txt
├── public
├── src
│   ├── components
│   │   ├──common
│   │   ├── stopwatch
│   │   ├── timer
│   │   ├── App.css
│   │   └── App.js
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

- Please complete this challenge in the `src/components/timer/Timer.js` file.
- The `onStart` function is called every second by the useEffect hook.
  - It checks if the timer has reached 0 hours, 0 minutes, and 0 seconds. If so, it sets isStarted to false and returns.
  - If the timer is not started, it returns without making any changes.
  - If the timer is running, it decrements the timer by 1 second. -
  - If the minutes or seconds reach 0, it adjusts the hours, minutes, or seconds accordingly using the setTimer function.
- The `onReset` function is called when the "Reset" button is clicked.
  - It sets isStarted to false and resets the timer to 0 hours, 0 minutes, and 0 seconds.

## Example

Once you have completed the code, run it with the following command:

```bash
npm start
```

The finished result is as follows:

![finished](./assets/finished.gif)
