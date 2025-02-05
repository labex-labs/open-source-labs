# Code Walk Through Object Keys

To generate a list of all the keys of a given object, use the following steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.

2. Define a generator function called `walk` that takes an object and an array of keys. Use recursion to walk through all the keys of the object.

3. Inside the `walk` function, use a `for...of` loop and `Object.keys()` to iterate over the keys of the object.

4. Use `typeof` to check if each value in the given object is itself an object. If the value is an object, use the `yield*` expression to recursively delegate to the same generator function, `walk`, appending the current `key` to the array of keys.

5. Otherwise, `yield` an array of keys representing the current path and the value of the given `key`.

6. Use the `yield*` expression to delegate to the `walk` generator function.

Here's the code:

```js
const walkThrough = function* (obj) {
  const walk = function* (x, previous = []) {
    for (let key of Object.keys(x)) {
      if (typeof x[key] === "object") yield* walk(x[key], [...previous, key]);
      else yield [[...previous, key], x[key]];
    }
  };
  yield* walk(obj);
};
```

To test the code, create an object and use the `walkThrough` function to generate a list of all its keys:

```js
const obj = {
  a: 10,
  b: 20,
  c: {
    d: 10,
    e: 20,
    f: [30, 40]
  },
  g: [
    {
      h: 10,
      i: 20
    },
    {
      j: 30
    },
    40
  ]
};
[...walkThrough(obj)];
/*
[
  [['a'], 10],
  [['b'], 20],
  [['c', 'd'], 10],
  [['c', 'e'], 20],
  [['c', 'f', '0'], 30],
  [['c', 'f', '1'], 40],
  [['g', '0', 'h'], 10],
  [['g', '0', 'i'], 20],
  [['g', '1', 'j'], 30],
  [['g', '2'], 40]
]
*/
```
