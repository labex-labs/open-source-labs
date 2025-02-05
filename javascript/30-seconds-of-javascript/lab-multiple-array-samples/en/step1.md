# Code Practice: Getting Random Elements from an Array

To practice coding, open the Terminal/SSH and type `node`. The following code utilizes the Fisher-Yates algorithm to shuffle an array and retrieve `n` random, unique elements at unique keys from the array, up to the size of the array.

```js
const sampleSize = ([...arr], n = 1) => {
  let m = arr.length;
  while (m) {
    const i = Math.floor(Math.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  }
  return arr.slice(0, n);
};
```

To use this code, call `sampleSize()` with an array and an optional number `n` of elements to retrieve. If `n` is not provided, the function will return only one element at random from the array.

```js
sampleSize([1, 2, 3], 2); // [3, 1]
sampleSize([1, 2, 3], 4); // [2, 3, 1]
```
