# Here's how to execute a function for each array element in reverse

To execute a function for each array element, starting from the array's last element, follow these steps:

1. Clone the given array using `Array.prototype.slice()`.
2. Reverse the cloned array using `Array.prototype.reverse()`.
3. Use `Array.prototype.forEach()` to iterate over the reversed array.

Here's an example code snippet:

```js
const forEachRight = (arr, callback) => arr.slice().reverse().forEach(callback);
```

You can test the function by running the following code:

```js
forEachRight([1, 2, 3, 4], (val) => console.log(val)); // '4', '3', '2', '1'
```

To get started with coding, open the Terminal/SSH and type `node`.
