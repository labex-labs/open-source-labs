# A function that gets the nth argument

To start practicing coding, open the Terminal/SSH and type `node`. Here's how you can create a function that gets the argument at index `n`.

- Use `Array.prototype.slice()` to get the desired argument at index `n`.
- If `n` is negative, the nth argument from the end is returned.

```js
const nthArg =
  (n) =>
  (...args) =>
    args.slice(n)[0];
```

Here's an example of how to use the `nthArg` function:

```js
const third = nthArg(2);
console.log(third(1, 2, 3)); // Output: 3
console.log(third(1, 2)); // Output: undefined

const last = nthArg(-1);
console.log(last(1, 2, 3, 4, 5)); // Output: 5
```
