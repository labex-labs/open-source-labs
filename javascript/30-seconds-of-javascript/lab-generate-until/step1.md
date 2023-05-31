# Generating Values Until a Given Condition is Met

To start practicing coding, open the Terminal/SSH and type `node`. Once you have done that, you can create a generator that produces new values until a given condition is met.

To create this generator, follow these steps:

- Initialize the current `val` using the `seed` value.
- Use a `while` loop to keep iterating while the `condition` function, called with the current `val`, returns `false`.
- Use the `yield` keyword to return the current `val` and, optionally, receive a new seed value, `nextSeed`.
- Use the `next` function to calculate the next value from the current `val` and the `nextSeed`.

Here's an example code snippet:

```js
const generateUntil = function* (seed, condition, next) {
  let val = seed;
  let nextSeed = null;
  while (!condition(val)) {
    nextSeed = yield val;
    val = next(val, nextSeed);
  }
  return val;
};
```

You can use the generator by calling it with the appropriate arguments. For example:

```js
[
  ...generateUntil(
    1,
    (v) => v > 5,
    (v) => ++v
  ),
]; // [1, 2, 3, 4, 5]
```

This will produce an array of values from `1` to `5`, since the condition `v > 5` is met when `val` equals `6`.
