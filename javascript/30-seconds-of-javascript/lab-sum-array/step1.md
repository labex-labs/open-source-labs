# Here's how to find the sum of an array

To find the sum of an array of numbers, follow these steps:

1. Open the Terminal/SSH and type `node` to start coding.
2. Use the `Array.prototype.reduce()` method to add each value to an accumulator, which should be initialized with a value of `0`.
3. Here's the code you can use to find the sum of the array:

```js
const sum = (...arr) => [...arr].reduce((acc, val) => acc + val, 0);
```

4. To test the `sum` function, use the following code examples:

```js
sum(1, 2, 3, 4); // 10
sum(...[1, 2, 3, 4]); // 10
```

By following these steps, you can easily find the sum of an array of numbers using JavaScript.
