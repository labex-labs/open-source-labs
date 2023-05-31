# How to Get Array Tail in JavaScript

To get all the elements in an array except for the first one, you can use the `Array.prototype.slice()` method. If the array length is more than 1, use `slice(1)` to return the array without the first element. Otherwise, return the whole array.

Here's an example code:

```js
const tail = (arr) => (arr.length > 1 ? arr.slice(1) : arr);
```

You can now use the `tail()` function to get the array tail:

```js
tail([1, 2, 3]); // [2, 3]
tail([1]); // [1]
```
