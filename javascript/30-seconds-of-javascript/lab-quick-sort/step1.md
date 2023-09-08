# Quick Sort Algorithm

To practice coding, open the Terminal/SSH and type `node`. This algorithm sorts an array of numbers using the quicksort algorithm. Here are the steps to follow:

- Use recursion.
- Use the spread operator (`...`) to clone the original array, `arr`.
- If the `length` of the array is less than `2`, return the cloned array.
- Use `Math.floor()` to calculate the index of the pivot element.
- Use `Array.prototype.reduce()` and `Array.prototype.push()` to split the array into two subarrays. The first one contains elements smaller than or equal to `pivot`, and the second one contains elements greater than it. Destructure the result into two arrays.
- Recursively call `quickSort()` on the created subarrays.

Here is an example of how to implement this algorithm:

```js
const quickSort = (arr) => {
  const a = [...arr];
  if (a.length < 2) return a;
  const pivotIndex = Math.floor(arr.length / 2);
  const pivot = a[pivotIndex];
  const [lo, hi] = a.reduce(
    (acc, val, i) => {
      if (val < pivot || (val === pivot && i != pivotIndex)) {
        acc[0].push(val);
      } else if (val > pivot) {
        acc[1].push(val);
      }
      return acc;
    },
    [[], []]
  );
  return [...quickSort(lo), pivot, ...quickSort(hi)];
};
```

To test it out, run the following command:

```js
quickSort([1, 6, 1, 5, 3, 2, 1, 4]); // [1, 1, 1, 2, 3, 4, 5, 6]
```
