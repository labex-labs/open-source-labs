# How to Pull Matching Values From an Array

To pull out specific values from an array using JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.filter()` and `Array.prototype.includes()` to filter out the values that are not needed and create a new array.
3. Set `Array.prototype.length` to mutate the original array by resetting its length to `0`.
4. Use `Array.prototype.push()` to re-populate the original array with only the pulled values.
5. Use `Array.prototype.push()` to keep track of the removed values in a new array.

Here's an example function that implements these steps:

```js
const pullAtValue = (arr, pullArr) => {
  let removed = [],
    pushToRemove = arr.forEach((v, i) =>
      pullArr.includes(v) ? removed.push(v) : v,
    ),
    mutateTo = arr.filter((v, i) => !pullArr.includes(v));
  arr.length = 0;
  mutateTo.forEach((v) => arr.push(v));
  return removed;
};
```

You can use this function to remove specific values from an array and return the removed elements like this:

```js
let myArray = ["a", "b", "c", "d"];
let pulled = pullAtValue(myArray, ["b", "d"]);
// myArray = [ 'a', 'c' ] , pulled = [ 'b', 'd' ]
```
