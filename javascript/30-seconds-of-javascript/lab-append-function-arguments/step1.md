# Function that Appends Arguments

To create a function that appends arguments to the ones it receives, follow these steps:

1. Open the Terminal/SSH and type `node` to start coding practice.
2. Use the spread operator (`...`) to append `partials` to the list of arguments of `fn`.
3. Use the following code to create the function:

```js
const partialRight =
  (fn, ...partials) =>
  (...args) =>
    fn(...args, ...partials);
```

4. Test the function with an example, such as:

```js
const greet = (greeting, name) => greeting + " " + name + "!";
const greetJohn = partialRight(greet, "John");
greetJohn("Hello"); // 'Hello John!'
```
