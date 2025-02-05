# Code Practice with Repeat Generator

To practice coding, open the Terminal/SSH and type `node` to create a generator that repeats the given value indefinitely. Use a non-terminating `while` loop that will `yield` a value every time `Generator.prototype.next()` is called. Then, use the return value of the `yield` statement to update the returned value if the passed value is not `undefined`.

```js
const repeatGenerator = function* (val) {
  let v = val;
  while (true) {
    let newV = yield v;
    if (newV !== undefined) v = newV;
  }
};
```

To test the generator, create an instance of it using the value `5` and call `repeater.next()` to get the next value in the sequence. The output will be `{ value: 5, done: false }`. Calling `repeater.next()` again will return the same value. To change the value, call `repeater.next(4)`, which will return `{ value: 4, done: false }`. Finally, calling `repeater.next()` will return the updated value, `{ value: 4, done: false }`.
