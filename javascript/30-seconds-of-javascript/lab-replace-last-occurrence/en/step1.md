# Understanding the Problem and Setting Up

Before we start coding, let us understand what our `replaceLast` function should do:

1. Accept three parameters:

   - `str`: The input string to modify
   - `pattern`: The substring or regular expression to search for
   - `replacement`: The string to replace the last occurrence with

2. Return a new string with the last occurrence of the pattern replaced.

Let us create a JavaScript file to implement our function:

1. Navigate to the project directory in the WebIDE file explorer.
2. Create a new file named `replaceLast.js` in the `replace-last` directory.
3. Add the following basic structure to the file:

```javascript
// Function to replace the last occurrence of a pattern in a string
function replaceLast(str, pattern, replacement) {
  // Our implementation will go here
  return str;
}

// We will add test cases here later
```

To check that everything is set up correctly, let us add a simple test:

```javascript
// Example usage
console.log(replaceLast("Hello world world", "world", "JavaScript"));
```

Now, let us run our code to see the current output:

1. Open the Terminal in WebIDE
2. Navigate to the `replace-last` directory:
   ```bash
   cd ~/project/replace-last
   ```
3. Run the JavaScript file using Node.js:
   ```bash
   node replaceLast.js
   ```

You should see `Hello world world` in the output because our function currently just returns the original string without making any changes.
