# Creating a Function to Validate ISO Formatted Date Strings

In this step, we will create a JavaScript function that checks if a given string is in valid ISO 8601 format.

## Creating the Validation Function

Let us create a new JavaScript file for our ISO date validator:

1. In the WebIDE, click on the Explorer icon in the left sidebar
2. Right-click in the file explorer and select "New File"
3. Name the file `isISODate.js` and press Enter
4. Add the following code to the file:

```javascript
/**
 * Checks if a string is a valid ISO 8601 formatted date string
 * @param {string} val - The string to check
 * @return {boolean} - Returns true if the string is in ISO format, false otherwise
 */
const isISOString = (val) => {
  // Create a Date object from the input string
  const d = new Date(val);

  // Check if the date is valid (not NaN) and if the ISO string matches the original
  return !Number.isNaN(d.valueOf()) && d.toISOString() === val;
};

// Export the function so we can use it elsewhere
module.exports = isISOString;
```

Let us examine how this function works:

1. `new Date(val)` creates a Date object from the input string
2. `d.valueOf()` returns the numeric timestamp value (milliseconds since January 1, 1970)
3. `Number.isNaN(d.valueOf())` checks if the date is invalid (NaN means "Not a Number")
4. `d.toISOString() === val` verifies that converting the Date back to an ISO string matches the original input

## Testing Our Function

Now, let us create a simple test file to try our function:

1. Create another file named `testISO.js`
2. Add the following code:

```javascript
// Import our isISOString function
const isISOString = require("./isISODate");

// Test with a valid ISO formatted date
console.log("Testing a valid ISO date:");
console.log("2020-10-12T10:10:10.000Z");
console.log("Result:", isISOString("2020-10-12T10:10:10.000Z"));
console.log();

// Test with an invalid format
console.log("Testing a non-ISO date:");
console.log("2020-10-12");
console.log("Result:", isISOString("2020-10-12"));
```

3. Run the test file using Node.js:

```bash
node testISO.js
```

You should see output similar to:

```
Testing a valid ISO date:
2020-10-12T10:10:10.000Z
Result: true

Testing a non-ISO date:
2020-10-12
Result: false
```

This shows our function correctly identifies that "2020-10-12T10:10:10.000Z" is a valid ISO formatted date, while "2020-10-12" is not.
