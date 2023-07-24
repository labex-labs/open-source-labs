# How to Get the Byte Size of a String in JavaScript

To get the byte size of a string in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Convert the string to a [`Blob` Object](https://developer.mozilla.org/en-US/docs/Web/API/Blob).
3. Use `Blob.size` to get the length of the string in bytes.

Here's the JavaScript code to get the byte size of a string:

```js
const byteSize = (str) => new Blob([str]).size;
```

You can test this function with the following examples:

```js
byteSize("😀"); // 4
byteSize("Hello World"); // 11
```
