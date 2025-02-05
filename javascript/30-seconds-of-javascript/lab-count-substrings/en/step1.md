# How to Count Substrings in a String using JavaScript

If you want to practice coding, open the Terminal/SSH and type `node`. This JavaScript function counts the number of occurrences of a specified substring in a given string.

To use this function, follow these steps:

1. Declare a function called `countSubstrings` that takes two parameters: `str` and `searchValue`.
2. Initialize two variables: `count` and `i`.
3. Use the `Array.prototype.indexOf()` method to search for `searchValue` in `str`.
4. If the value is found, increment the `count` variable and update the `i` variable.
5. Use a `while` loop that returns as soon as the value returned from `Array.prototype.indexOf()` is `-1`.
6. Return the `count` variable.

Here's the code for the `countSubstrings` function:

```js
const countSubstrings = (str, searchValue) => {
  let count = 0,
    i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) [count, i] = [count + 1, r + 1];
    else return count;
  }
};
```

You can test the function using the examples below:

```js
countSubstrings("tiktok tok tok tik tok tik", "tik"); // 3
countSubstrings("tutut tut tut", "tut"); // 4
```
