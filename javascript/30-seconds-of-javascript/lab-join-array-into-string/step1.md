# How to Join an Array Into a String

To join all the elements of an array into a string, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the function `join()` with the following parameters:
   - `arr`: the array to be joined.
   - `separator` (optional): the separator to be used between the elements of the array. If not specified, the default separator `,` will be used.
   - `end` (optional): the separator to be used between the last two elements of the array. If not specified, the same value as `separator` will be used by default.
3. The `join()` function uses `Array.prototype.reduce()` to combine the elements of the array into a string.
4. The final string is returned.

Here's the code for the `join()` function:

```js
const join = (arr, separator = ",", end = separator) =>
  arr.reduce(
    (acc, val, i) =>
      i === arr.length - 2
        ? acc + val + end
        : i === arr.length - 1
        ? acc + val
        : acc + val + separator,
    "",
  );
```

And here are some examples of how to use the `join()` function:

```js
join(["pen", "pineapple", "apple", "pen"], ",", "&"); // 'pen,pineapple,apple&pen'
join(["pen", "pineapple", "apple", "pen"], ","); // 'pen,pineapple,apple,pen'
join(["pen", "pineapple", "apple", "pen"]); // 'pen,pineapple,apple,pen'
```
