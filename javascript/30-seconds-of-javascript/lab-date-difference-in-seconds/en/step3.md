# Implementing the Date Difference Function Using Arrow Functions

Now that we understand how to calculate date differences, let us implement a more concise version of our function using arrow functions.

## Arrow Functions in JavaScript

Arrow functions provide a shorter syntax for writing functions in JavaScript. Here is how we can rewrite our date difference function using arrow function syntax:

```javascript
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;
```

This function does exactly the same thing as our previous function, but with a cleaner and more concise syntax.

## Creating a JavaScript File

Let us create a JavaScript file to store and test our function. Exit the Node.js environment by pressing Ctrl+D or typing `.exit` and pressing Enter.

Now, create a new file named `dateDifference.js` in the WebIDE:

1. Click on the "Explorer" icon on the left sidebar
2. Right-click in the file explorer and select "New File"
3. Name the file `dateDifference.js` and press Enter
4. Add the following code to the file:

```javascript
// Function to calculate difference between two dates in seconds
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// Test examples
console.log("Example 1:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:15"),
    new Date("2020-12-24 00:00:17")
  )
); // Expected output: 2

console.log("\nExample 2:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:00"),
    new Date("2020-12-24 00:01:00")
  )
); // Expected output: 60

console.log("\nExample 3:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:00"),
    new Date("2020-12-24 01:00:00")
  )
); // Expected output: 3600
```

Save the file by pressing Ctrl+S or by clicking File > Save.

## Running the JavaScript File

To run the file we just created, use the following command in the terminal:

```bash
node dateDifference.js
```

You should see the following output:

```
Example 1:
2

Example 2:
60

Example 3:
3600
```

This confirms that our function is working correctly:

- First example: The difference between 00:00:15 and 00:00:17 is 2 seconds
- Second example: The difference between 00:00:00 and 00:01:00 is 60 seconds (1 minute)
- Third example: The difference between 00:00:00 and 01:00:00 is 3600 seconds (1 hour)
