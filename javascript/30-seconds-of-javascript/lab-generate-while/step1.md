# Generator That Produces Values While a Condition is True

To start coding, open the Terminal/SSH and type `node`. This will create a generator that keeps producing new values as long as the given condition is met.

The generator is initialized with a `seed` value, which is used to initialize the current `val`. A `while` loop is then used to iterate while the `condition` function called with the current `val` returns `true`.

The `yield` keyword is used to return the current `val` and optionally receive a new seed value, `nextSeed`. The `next` function is used to calculate the next value from the current `val` and the `nextSeed`.

```js
const generateWhile = function* (seed, condition, next) {
  let val = seed;
  let nextSeed = null;
  while (condition(val)) {
    nextSeed = yield val;
    val = next(val, nextSeed);
  }
  return val;
};
```

To use the generator, call it with the `seed`, `condition`, and `next` functions. For example, calling `[...generateWhile(1, v => v <= 5, v => ++v)]` will return `[1, 2, 3, 4, 5]`.
