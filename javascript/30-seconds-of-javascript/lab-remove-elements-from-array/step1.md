# Removing Elements From Array

To remove elements from an array, you can use the `Array.prototype.splice()` method, which mutates the original array, or you can use the `shank` function provided below, which returns a new array.

## Shank Function

The `shank` function has the following syntax:

```js
const shank = (arr, index = 0, delCount = 0, ...elements) => {
  // code goes here
};
```

- `arr`: the array to modify.
- `index`: the index at which to start removing elements. If omitted, it defaults to `0`.
- `delCount`: the number of elements to remove. If omitted, it defaults to `0`.
- `elements`: the elements to insert at the `index` position. If omitted, no elements are added.

The `shank` function uses `Array.prototype.slice()` and `Array.prototype.concat()` to get a new array with the new contents after removing existing elements and/or adding new elements.

## Examples

```js
const names = ["alpha", "bravo", "charlie"];
const namesAndDelta = shank(names, 1, 0, "delta");
console.log(namesAndDelta); // [ 'alpha', 'delta', 'bravo', 'charlie' ]

const namesNoBravo = shank(names, 1, 1);
console.log(namesNoBravo); // [ 'alpha', 'charlie' ]

console.log(names); // ['alpha', 'bravo', 'charlie']
```

In the first example, the `shank` function inserts the string `'delta'` at index `1` of the `names` array, resulting in a new array with the elements `['alpha', 'delta', 'bravo', 'charlie']`.

In the second example, the `shank` function removes the element at index `1` of the `names` array, resulting in a new array with the elements `['alpha', 'charlie']`.

Note that the original `names` array is not modified by either call to the `shank` function.
