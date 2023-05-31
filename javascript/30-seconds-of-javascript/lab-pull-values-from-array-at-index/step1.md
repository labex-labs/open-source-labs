# How to Pull Values From Array at Index

To pull out specific values from an array at certain indexes, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.filter()` and `Array.prototype.includes()` to filter out the values that are not needed and store them in a new array called `removed`.
3. Set `Array.prototype.length` to `0` to mutate the original array by resetting its length.
4. Use `Array.prototype.push()` to re-populate the original array with only the pulled values.
5. Use `Array.prototype.push()` to keep track of the removed values.
6. The function `pullAtIndex` takes two arguments: the original array and an array of indexes to pull out.
7. The function returns an array of removed values.

Example usage:

```js
const pullAtIndex = (arr, pullArr) => {
  let removed = [];
  let pulled = arr
    .map((v, i) => (pullArr.includes(i) ? removed.push(v) : v))
    .filter((v, i) => !pullArr.includes(i));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
  return removed;
};

let myArray = ["a", "b", "c", "d"];
let pulled = pullAtIndex(myArray, [1, 3]);
// myArray = [ 'a', 'c' ] , pulled = [ 'b', 'd' ]
```
