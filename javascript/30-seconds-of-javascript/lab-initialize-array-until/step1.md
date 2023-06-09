# How to Initialize an Array Until a Condition is Met

To start practicing coding, open the Terminal/SSH and type `node`.

Here are the steps to initialize and fill an array with values generated by a function until a certain condition is met:

1. Create an empty array `arr`, an index variable `i`, and an element `el`.
2. Use a `do...while` loop to add elements to the array using the `mapFn` function until the `conditionFn` function returns `true` for the given index `i` and element `el`.
3. The `conditionFn` function takes three arguments: the current index, the previous element, and the array itself.
4. The `mapFn` function takes three arguments: the current index, the current element, and the array itself.

Here's the code:

```js
const initializeArrayUntil = (conditionFn, mapFn) => {
  const arr = [];
  let i = 0;
  let el = undefined;
  do {
    el = mapFn(i, el, arr);
    arr.push(el);
    i++;
  } while (!conditionFn(i, el, arr));
  return arr;
};
```

To use the `initializeArrayUntil` function, provide two functions as arguments:

```js
initializeArrayUntil(
  (i, val) => val > 10, //conditionFn
  (i, val, arr) => (i <= 1 ? 1 : val + arr[i - 2]) //mapFn
); // [1, 1, 2, 3, 5, 8, 13]
```

This code initializes an array with the Fibonacci sequence up to the first number greater than 10. The `conditionFn` function checks if the current value is greater than 10, and the `mapFn` function generates the next number in the sequence.
