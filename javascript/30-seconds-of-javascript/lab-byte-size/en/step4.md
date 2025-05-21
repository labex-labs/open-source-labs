# Creating a Practical Example File

Now let's create a JavaScript file to implement our byte size function in a more practical way. This will demonstrate how you might use this function in a real-world application.

1. Create a new file in the WebIDE. Click on the "New File" icon in the file explorer sidebar, and name it `byteSizeCalculator.js`.

2. Add the following code to the file:

```javascript
/**
 * Calculate the byte size of a given string.
 * @param {string} str - The string to calculate the byte size for.
 * @returns {number} The size in bytes.
 */
function calculateByteSize(str) {
  return new Blob([str]).size;
}

// Examples with different types of strings
const examples = [
  "Hello World",
  "😀",
  "The quick brown fox jumps over the lazy dog",
  "123!@#$%^&*()",
  "Hello, 世界！",
  "😀😃😄😁"
];

// Display the results
console.log("String Byte Size Calculator\n");
console.log("String".padEnd(45) + "| Characters | Bytes");
console.log("-".repeat(70));

examples.forEach((example) => {
  console.log(
    `"${example}"`.padEnd(45) +
      `| ${example.length}`.padEnd(12) +
      `| ${calculateByteSize(example)}`
  );
});
```

3. Save the file by pressing Ctrl+S or by selecting File > Save from the menu.

4. Run the file from the terminal:

```bash
node byteSizeCalculator.js
```

You should see output similar to this:

```
String Byte Size Calculator

String                                      | Characters | Bytes
----------------------------------------------------------------------
"Hello World"                               | 11         | 11
"😀"                                        | 1          | 4
"The quick brown fox jumps over the lazy dog" | 43         | 43
"123!@#$%^&*()"                            | 13         | 13
"Hello, 世界!"                              | 10         | 13
"😀😃😄😁"                                  | 4          | 16
```

This table clearly shows the difference between character count and byte size for different types of strings.

Understanding these differences is crucial when:

- Setting limits on user input in web forms
- Calculating storage requirements for text data
- Working with APIs that have size limitations
- Optimizing data transfer over networks
