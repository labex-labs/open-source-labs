# Merge Sort Algorithm

To practice coding using the merge sort algorithm, follow these steps:

1. Open Terminal/SSH and type `node`.
2. Use recursion to sort an array of numbers.
3. If the `length` of the array is less than `2`, return the array.
4. Use `Math.floor()` to calculate the middle point of the array.
5. Use `Array.prototype.slice()` to slice the array in two and recursively call `mergeSort()` on the created subarrays.
6. Finally, use `Array.from()` and `Array.prototype.shift()` to combine the two sorted subarrays into one.

Here's the code:

```js
const mergeSort = (arr) => {
  if (arr.length < 2) return arr;
  const mid = Math.floor(arr.length / 2);
  const l = mergeSort(arr.slice(0, mid));
  const r = mergeSort(arr.slice(mid, arr.length));
  return Array.from({ length: l.length + r.length }, () => {
    if (!l.length) return r.shift();
    else if (!r.length) return l.shift();
    else return l[0] > r[0] ? r.shift() : l.shift();
  });
};
```

Try it out with this example:

```js
mergeSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```
