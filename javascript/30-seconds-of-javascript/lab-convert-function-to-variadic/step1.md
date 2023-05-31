# Converting a Function to a Variadic Function

To convert a function that accepts an array into a variadic function, you can follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.

2. Return a closure that collects all inputs into an array-accepting function.

```js
const collectInto =
  (fn) =>
  (...args) =>
    fn(args);
```

3. Use the `collectInto` function to convert a function to a variadic function.

```js
const Pall = collectInto(Promise.all.bind(Promise));
let p1 = Promise.resolve(1);
let p2 = Promise.resolve(2);
let p3 = new Promise((resolve) => setTimeout(resolve, 2000, 3));
Pall(p1, p2, p3).then(console.log); // [1, 2, 3] (after about 2 seconds)
```

This will allow you to accept any number of arguments in your function and collect them into an array for further processing.
