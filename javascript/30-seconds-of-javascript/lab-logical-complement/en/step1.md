# Logical Complement

To begin practicing coding, open the Terminal/SSH and type `node`.

To get the logical complement of a function `fn`, use the `complement` function. This function returns another function that applies the logical not (`!`) operator on the result of calling `fn` with any arguments supplied.

Here's an example code snippet:

```js
const complement =
  (fn) =>
  (...args) =>
    !fn(...args);
```

To use this function, define a predicate function, for instance, `isEven` that returns `true` if a given number is even. You can then get the logical complement of this function using the `complement` function, as shown below:

```js
const isEven = (num) => num % 2 === 0;
const isOdd = complement(isEven);
isOdd(2); // false
isOdd(3); // true
```
