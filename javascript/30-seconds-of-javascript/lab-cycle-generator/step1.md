# Cycle Generator Instructions

To start practicing coding, open the Terminal/SSH and type `node`. Afterward, create a generator that loops over the given array indefinitely. Here are the steps:

1. Use a non-terminating `while` loop that will `yield` a value each time `Generator.prototype.next()` is called.
2. Use the module operator (`%`) with `Array.prototype.length` to get the next value's index and increment the counter after each `yield` statement.

Here's an example of the `cycleGenerator` function:

```js
const cycleGenerator = function* (arr) {
  let i = 0;
  while (true) {
    yield arr[i % arr.length];
    i++;
  }
};
```

You can then use the function as follows:

```js
const binaryCycle = cycleGenerator([0, 1]);
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
```

With these instructions, you can create a cycle generator that loops over any array indefinitely.
