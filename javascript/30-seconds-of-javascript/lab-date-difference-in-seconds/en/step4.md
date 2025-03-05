# Creating a Practical Application

Now that we have a working function to calculate the difference between dates in seconds, let us create a more practical application. We will build a simple timer that calculates how much time has passed since we started it.

## Creating a Timer Application

Create a new file named `timer.js` in the WebIDE:

1. Click on the "Explorer" icon on the left sidebar
2. Right-click in the file explorer and select "New File"
3. Name the file `timer.js` and press Enter
4. Add the following code to the file:

```javascript
// Function to calculate difference between two dates in seconds
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// Start time - when the script starts running
const startTime = new Date();
console.log(`Timer started at: ${startTime.toLocaleTimeString()}`);

// Function to update and display the elapsed time
function updateTimer() {
  const currentTime = new Date();
  const elapsedSeconds = getSecondsDiffBetweenDates(startTime, currentTime);

  // Format the time as hours:minutes:seconds
  const hours = Math.floor(elapsedSeconds / 3600);
  const minutes = Math.floor((elapsedSeconds % 3600) / 60);
  const seconds = Math.floor(elapsedSeconds % 60);

  const formattedTime = `${hours.toString().padStart(2, "0")}:${minutes.toString().padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;

  // Clear the console and display the updated time
  console.clear();
  console.log(`Timer started at: ${startTime.toLocaleTimeString()}`);
  console.log(`Elapsed time: ${formattedTime}`);
}

// Update the timer every second
console.log("Timer is running... Press Ctrl+C to stop.");
const timerInterval = setInterval(updateTimer, 1000);

// Keep the script running
setTimeout(() => {
  clearInterval(timerInterval);
  console.log("\nTimer stopped after 1 minute.");
}, 60000); // Run for 1 minute
```

Save the file by pressing Ctrl+S or by clicking File > Save.

## Running the Timer Application

To run the timer application, use the following command in the terminal:

```bash
node timer.js
```

The timer will start and update every second, showing how much time has passed since it started. The timer will automatically stop after 1 minute, or you can stop it earlier by pressing Ctrl+C.

## Understanding the Timer Application

Let us break down how the timer application works:

1. We define the `getSecondsDiffBetweenDates` function to calculate the time difference in seconds.
2. We record the start time when the script begins running.
3. We define an `updateTimer` function that:
   - Gets the current time
   - Calculates how many seconds have passed since the start time
   - Formats the elapsed time as hours:minutes:seconds
   - Displays the formatted time
4. We use `setInterval` to run the `updateTimer` function every 1000 milliseconds (1 second).
5. We use `setTimeout` to stop the timer after 60000 milliseconds (1 minute).

This application demonstrates a practical use of our date difference function to create a real-time timer.
