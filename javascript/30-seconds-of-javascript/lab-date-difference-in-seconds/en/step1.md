# Getting Started with JavaScript Date Objects

JavaScript provides a built-in `Date` object that allows us to work with dates and times. Before we calculate the difference between dates, let us first understand how to create and work with Date objects in JavaScript.

## Starting the Node.js Environment

Let us begin by opening the interactive Node.js environment:

1. Open the Terminal by clicking on the Terminal menu at the top of the WebIDE
2. Type the following command and press Enter:

```bash
node
```

You should now see the Node.js prompt (`>`), indicating that you are in the JavaScript interactive environment. This allows you to execute JavaScript code directly in the terminal.

## Creating Date Objects

In JavaScript, we can create a new Date object in several ways:

```javascript
// Current date and time
let now = new Date();
console.log(now);

// Specific date and time (year, month [0-11], day, hour, minute, second)
let specificDate = new Date(2023, 0, 15, 10, 30, 45); // January 15, 2023, 10:30:45
console.log(specificDate);

// Date from string
let dateFromString = new Date("2023-01-15T10:30:45");
console.log(dateFromString);
```

Try typing each of these examples in the Node.js environment and observe the output.

Note that in JavaScript, months are zero-indexed, meaning January is 0, February is 1, and so on.

## Getting Timestamp from Date Objects

Every Date object in JavaScript internally stores time as the number of milliseconds that have passed since January 1, 1970 (UTC). This is known as a timestamp.

```javascript
let now = new Date();
console.log(now.getTime()); // Get timestamp in milliseconds
```

This timestamp will be useful for calculating the difference between dates.
