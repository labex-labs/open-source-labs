# Understanding Alphanumeric Characters

Alphanumeric characters consist of the 26 letters in the English alphabet (both uppercase A-Z and lowercase a-z) and the 10 numerical digits (0-9). When we check if a string is alphanumeric, we are verifying that it contains only these characters and nothing else.

In JavaScript, we can check for alphanumeric characters using regular expressions. Regular expressions (regex) are patterns used to match character combinations in strings.

Let's start by opening our code editor. In the WebIDE, navigate to the file explorer on the left side and create a new JavaScript file:

1. Right-click in the file explorer panel
2. Select "New File"
3. Name the file `alphanumeric.js`

Once you have created the file, it should open automatically in the editor. If not, click on `alphanumeric.js` in the file explorer to open it.

![new-file](../assets/screenshot-20250306-K5AOWF7Z@2x.png)

Now, let's enter the following code:

```javascript
// Function to check if a string is alphanumeric
function isAlphaNumeric(str) {
  // Using regular expression to check for alphanumeric characters
  return /^[a-zA-Z0-9]+$/.test(str);
}

// Example usage
console.log("Is 'hello123' alphanumeric?", isAlphaNumeric("hello123"));
console.log("Is '123' alphanumeric?", isAlphaNumeric("123"));
console.log("Is 'hello 123' alphanumeric?", isAlphaNumeric("hello 123"));
console.log("Is 'hello@123' alphanumeric?", isAlphaNumeric("hello@123"));
```

Save the file by pressing `Ctrl+S` or by selecting "File" > "Save" from the menu.

Now, let's run this JavaScript file to see the output. Open the terminal in the WebIDE by selecting "Terminal" > "New Terminal" from the menu or by pressing `` Ctrl+` ``.

In the terminal, execute the following command:

```bash
node alphanumeric.js
```

You should see the following output:

```
Is 'hello123' alphanumeric? true
Is '123' alphanumeric? true
Is 'hello 123' alphanumeric? false
Is 'hello@123' alphanumeric? false
```

This output shows that our function correctly identifies `hello123` and `123` as alphanumeric strings, while `hello 123` (contains a space) and `hello@123` (contains a special character @) are not alphanumeric.
