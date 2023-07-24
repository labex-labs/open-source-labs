# Index of Substrings

To find all the indexes of a substring in a given string, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the built-in method `Array.prototype.indexOf()` to search for `searchValue` in `str`.
3. Use `yield` to return the index if the value is found and update the index, `i`.
4. Use a `while` loop that will terminate the generator as soon as the value returned from `Array.prototype.indexOf()` is `-1`.

Here's an example code to implement the above steps:

```js
const indexOfSubstrings = function* (str, searchValue) {
  let i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) {
      yield r;
      i = r + 1;
    } else return;
  }
};
```

You can test the function with the following code:

```js
[...indexOfSubstrings("tiktok tok tok tik tok tik", "tik")]; // [0, 15, 23]
[...indexOfSubstrings("tutut tut tut", "tut")]; // [0, 2, 6, 10]
[...indexOfSubstrings("hello", "hi")]; // []
```
