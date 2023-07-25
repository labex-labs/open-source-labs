# Using Argument Coalescing

To start coding, open the Terminal/SSH and type `node`. Argument coalescing is a technique used to return the first defined, non-null argument in a list of arguments. To achieve this, use `Array.prototype.find()` and `Array.prototype.includes()` to find the first value that is not equal to `undefined` or `null`.

Here's an example of how to use argument coalescing in JavaScript:

```js
const coalesce = (...args) => args.find((v) => ![undefined, null].includes(v));
```

In the above code snippet, `coalesce` is a function that takes any number of arguments and returns the first defined, non-null argument. Here's an example of how to use the `coalesce` function:

```js
coalesce(null, undefined, "", NaN, "Waldo"); // ''
```

In this example, `coalesce` is called with a list of arguments that includes `null`, `undefined`, an empty string `''`, `NaN`, and the string `'Waldo'`. The function returns an empty string `''` because it is the first defined, non-null argument in the list.
