# Function to Copy a String to the Clipboard

To copy a string to the clipboard, use the `copyToClipboardAsync` function. The function returns a promise that resolves when the clipboard's contents have been updated. Here are the steps:

1. Check if the Clipboard API is available by verifying if `Navigator`, `Navigator.clipboard`, and `Navigator.clipboard.writeText` are truthy using an `if` statement.
2. If the Clipboard API is available, use `Clipboard.writeText()` to write the given value, `str`, to the clipboard.
3. Return the result of `Clipboard.writeText()`, which is a promise that resolves when the clipboard's contents have been updated.
4. If the Clipboard API is not available, reject the promise with an appropriate error message using `Promise.reject()`.
5. If you need to support older browsers, use `Document.execCommand()` instead of `Clipboard.writeText()`. You can find out more about it in the `copyToClipboard` snippet.

Here's the `copyToClipboardAsync` function:

```js
const copyToClipboardAsync = (str) => {
  if (navigator && navigator.clipboard && navigator.clipboard.writeText) {
    return navigator.clipboard.writeText(str);
  }
  return Promise.reject("The Clipboard API is not available.");
};
```

To use the function, call `copyToClipboardAsync` with the string you want to copy as an argument, like this:

```js
copyToClipboardAsync("Lorem ipsum"); // 'Lorem ipsum' copied to clipboard.
```
