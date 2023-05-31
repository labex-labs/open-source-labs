# A Function That Calls or Returns Another Function

To begin practicing coding, open the Terminal/SSH and type `node`.

Here's a function called `callOrReturn` that takes an argument and calls it if it's a function, otherwise, it returns it. Here's how it works:

- The function takes two parameters: `fn` and `...args`. `fn` is the argument to be checked, and `...args` is the list of arguments to be passed to the function if it's called.
- It uses the `typeof` operator to check if the given argument is a function.
- If the argument is indeed a function, it calls the function using the spread operator (`...`) to pass the rest of the given arguments. Otherwise, it simply returns the argument.
- Here's an example of how to use the `callOrReturn` function:

```js
const callOrReturn = (fn, ...args) =>
  typeof fn === "function" ? fn(...args) : fn;

callOrReturn((x) => x + 1, 1); // 2
callOrReturn(1, 1); // 1
```

In the first example, `callOrReturn(x => x + 1, 1)` calls the function `x => x + 1` with the argument `1`, which returns `2`. In the second example, `callOrReturn(1, 1)` simply returns `1` since it's not a function.
