# Selection Sort Algorithm

To start coding, open the Terminal/SSH and type `node`.

The following function sorts an array of numbers using the selection sort algorithm:

```js
const selectionSort = (arr) => {
  const a = [...arr];
  for (let i = 0; i < a.length; i++) {
    const min = a
      .slice(i + 1)
      .reduce((acc, val, j) => (val < a[acc] ? j + i + 1 : acc), i);
    if (min !== i) [a[i], a[min]] = [a[min], a[i]];
  }
  return a;
};
```

To use the function, pass an array of numbers to `selectionSort()`, like this:

```js
selectionSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```

The function works by cloning the original array using the spread operator (`...`). It then iterates over the array using a `for` loop. Using `Array.prototype.slice()` and `Array.prototype.reduce()`, it finds the index of the minimum element in the subarray to the right of the current index. If necessary, it performs a swap.
