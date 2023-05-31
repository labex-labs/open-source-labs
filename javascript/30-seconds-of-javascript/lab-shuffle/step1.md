# Array Shuffling Algorithm

To shuffle an array in JavaScript, use the Fisher-Yates algorithm. This algorithm reorders the elements of the array randomly and returns a new array.

To start practicing coding, open the Terminal/SSH and type `node`.

Here's the code for the Fisher-Yates algorithm:

```js
const shuffle = ([...arr]) => {
  let m = arr.length;
  while (m) {
    const i = Math.floor(Math.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  }
  return arr;
};
```

To shuffle an array, pass the array to the `shuffle` function and it will return the shuffled array. For example:

```js
const foo = [1, 2, 3];
shuffle(foo); // returns [2, 3, 1], and foo is still [1, 2, 3]
```
