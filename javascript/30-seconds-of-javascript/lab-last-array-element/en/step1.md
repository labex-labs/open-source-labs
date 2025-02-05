# How to Get the Last Element of an Array in JavaScript

To get started with coding, open the Terminal/SSH and type `node`. The following function returns the last element in an array:

```js
const last = (arr) => (arr && arr.length ? arr[arr.length - 1] : undefined);
```

To use it, you need to provide an array as an argument. The function checks if the array is truthy and has a `length` property. If both conditions are true, it computes the index of the last element of the array and returns it. Otherwise, it returns `undefined`.

Here are some examples:

```js
last([1, 2, 3]); // 3
last([]); // undefined
last(null); // undefined
last(undefined); // undefined
```
