# Code Practice

To start practicing coding, open the Terminal/SSH and type `node`. Then, you can use the `generateItems` function to generate an array with a specific number of items.

- Call `generateItems` with the desired number of items and a function that will be used to generate the items.
- `generateItems` uses `Array.from()` to create an empty array of the specified length, and calls the provided function with the index of each newly created element.
- The provided function takes one argument - the index of each element.

```js
const generateItems = (n, fn) => Array.from({ length: n }, (_, i) => fn(i));
```

Here's an example of using `generateItems` to generate an array of 10 random numbers:

```js
generateItems(10, Math.random);
// [0.21, 0.08, 0.40, 0.96, 0.96, 0.24, 0.19, 0.96, 0.42, 0.70]
```
