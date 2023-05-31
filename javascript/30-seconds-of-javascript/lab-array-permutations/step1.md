# How to Generate All Array Permutations

To start practicing coding, open the Terminal/SSH and type `node`.

Here's an algorithm that generates all permutations of an array's elements (even if it contains duplicates). Follow these steps to implement it:

1. Use recursion.
2. For each element in the given array, create all the partial permutations for the rest of its elements.
3. Use `Array.prototype.map()` to combine the element with each partial permutation, then `Array.prototype.reduce()` to combine all permutations in one array.
4. The base cases are for arrays with a length of `2` or `1`.
5. Beware that this function's execution time increases exponentially with each array element. Anything more than 8 to 10 entries may cause your browser to hang as it tries to solve all the different combinations.

Here's the code:

```js
const permutations = (arr) => {
  if (arr.length <= 2) return arr.length === 2 ? [arr, [arr[1], arr[0]]] : arr;
  return arr.reduce(
    (acc, item, i) =>
      acc.concat(
        permutations([...arr.slice(0, i), ...arr.slice(i + 1)]).map((val) => [
          item,
          ...val,
        ])
      ),
    []
  );
};
```

You can test the code by calling the `permutations()` function with an array argument:

```js
permutations([1, 33, 5]);
// [ [1, 33, 5], [1, 5, 33], [33, 1, 5], [33, 5, 1], [5, 1, 33], [5, 33, 1] ]
```
