# How to Create a Function with a Specific Number of Arguments

To create a function that accepts a specific number of arguments and ignores any additional arguments, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.

2. Use the following code to create your function:

```js
const ary =
  (fn, n) =>
  (...args) =>
    fn(...args.slice(0, n));
```

3. Call the function you just created, `ary`, with two arguments: the function you want to limit the arguments for (`fn`) and the number of arguments you want to limit it to (`n`).

4. Now you can use the new function to limit the number of arguments for any function you want. To do this, call your new function with the spread operator (`...`) and the arguments you want to limit.

Here's an example of how to use your new function:

```js
const firstTwoMax = ary(Math.max, 2);
[[2, 6, "a"], [6, 4, 8], [10]].map((x) => firstTwoMax(...x)); // [6, 6, 10]
```

In this example, `firstTwoMax` is a new function that limits the `Math.max` function to only accept the first two arguments. The `map` method is used to apply the new function to each array in the outer array, returning the maximum of the first two elements of each inner array.
