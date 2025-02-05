# Converting a Variadic Function

To convert a variadic function, follow these steps:

1. Open the Terminal/SSH and type `node` to start coding.
2. Create a function that takes a variadic function.
3. Use a closure and the spread operator (`...`) to map the array of arguments to the inputs of the function.
4. Return a new function that accepts an array of arguments and calls the original variadic function with those arguments.

Here's an example of how to use this technique to convert the `Math.max` function:

```js
const spreadOver = (fn) => (argsArr) => fn(...argsArr);

const arrayMax = spreadOver(Math.max);
arrayMax([1, 2, 3]); // 3
```
