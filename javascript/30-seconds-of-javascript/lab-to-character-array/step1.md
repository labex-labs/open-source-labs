# How to Convert a String to an Array of Characters in JavaScript

To convert a string to an array of characters in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the spread operator (`...`) to convert the string into an array of characters.
3. Define a function called `toCharArray` that takes a string as an argument and returns an array of its characters.
4. Call the `toCharArray` function with the string you want to convert as the argument.
5. The function will return an array of characters.

Here's the code:

```js
const toCharArray = (s) => [...s];

toCharArray("hello"); // ['h', 'e', 'l', 'l', 'o']
```
