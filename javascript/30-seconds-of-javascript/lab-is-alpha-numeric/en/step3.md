# Creating a Simple Validation Tool

Now that we understand the alphanumeric check function, let's build a simple interactive validation tool. We'll use Node.js's built-in `readline` module to get user input from the terminal.

Create a new file named `validator.js` in the same directory:

1. Right-click in the file explorer panel
2. Select "New File"
3. Name the file `validator.js`

Add the following code to the file:

```javascript
const readline = require("readline");

// Create a readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Function to check if a string is alphanumeric
function isAlphaNumeric(str) {
  return /^[a-zA-Z0-9]+$/.test(str);
}

// Function to check the input
function checkInput(input) {
  if (isAlphaNumeric(input)) {
    console.log(`"${input}" is alphanumeric.`);
  } else {
    console.log(`"${input}" is NOT alphanumeric.`);
    console.log(
      "Alphanumeric strings contain only letters (A-Z, a-z) and numbers (0-9)."
    );
  }

  // Ask if the user wants to check another string
  rl.question("\nDo you want to check another string? (yes/no): ", (answer) => {
    if (answer.toLowerCase() === "yes" || answer.toLowerCase() === "y") {
      askForInput();
    } else {
      console.log("Thank you for using the alphanumeric validator!");
      rl.close();
    }
  });
}

// Function to ask for input
function askForInput() {
  rl.question("Enter a string to check if it is alphanumeric: ", (input) => {
    checkInput(input);
  });
}

// Welcome message
console.log("=== Alphanumeric String Validator ===");
console.log(
  "This tool checks if a string contains only alphanumeric characters (A-Z, a-z, 0-9).\n"
);

// Start the program
askForInput();
```

Save the file and run it with:

```bash
node validator.js
```

You will see a welcome message and a prompt asking you to enter a string. Try entering different strings, such as:

- `hello123` (alphanumeric)
- `Hello World` (not alphanumeric due to the space)
- `hello@123` (not alphanumeric due to the @ symbol)

For each input, the program will tell you whether it's alphanumeric and will ask if you want to check another string. Type `yes` or `y` to continue, or any other response to exit the program.

This interactive tool demonstrates how our alphanumeric validation function can be used in a practical application.
