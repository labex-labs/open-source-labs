# Insertion Sort Algorithm in JavaScript

To practice coding, open the Terminal/SSH and type `node`. This algorithm sorts an array of numbers using the insertion sort method. Follow these steps to implement this algorithm:

1. Use `Array.prototype.reduce()` to iterate over all the elements in the given array.
2. If the `length` of the accumulator is `0`, add the current element to it.
3. Use `Array.prototype.some()` to iterate over the results in the accumulator until the correct position is found.
4. Use `Array.prototype.splice()` to insert the current element into the accumulator.

Here's the code to implement insertion sort in JavaScript:

```js
const insertionSort = (arr) =>
  arr.reduce((acc, x) => {
    if (!acc.length) return [x];
    acc.some((y, j) => {
      if (x <= y) {
        acc.splice(j, 0, x);
        return true;
      }
      if (x > y && j === acc.length - 1) {
        acc.splice(j + 1, 0, x);
        return true;
      }
      return false;
    });
    return acc;
  }, []);
```

You can test the algorithm with the following code:

```js
insertionSort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
