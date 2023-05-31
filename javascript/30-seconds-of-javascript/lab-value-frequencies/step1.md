# Instructions for Counting Value Frequencies

To count the frequency of values in an array, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Array.prototype.reduce()` method to map unique values to an object's keys, adding to existing keys every time the same value is encountered. This will create an object with the unique values of the array as keys and their frequencies as the values.
3. The code for this operation is as follows:

```js
const frequencies = (arr) =>
  arr.reduce((a, v) => {
    a[v] = a[v] ? a[v] + 1 : 1;
    return a;
  }, {});
```

4. To use this function, call `frequencies` with the array as its argument. For example:

```js
frequencies(["a", "b", "a", "c", "a", "a", "b"]); // { a: 4, b: 2, c: 1 }
frequencies([..."ball"]); // { b: 1, a: 1, l: 2 }
```

With these instructions, you can easily count the frequency of values in any given array.
