# Explanation of Juxtapose Functions

To use the `juxt` function, first open the Terminal/SSH and type `node` to start practicing coding. The `juxt` function takes several functions as arguments and returns a function that is the juxtaposition of those functions.

To create the `juxt` function, use `Array.prototype.map()` to return a `fn` that can take a variable number of `args`. When `fn` is called, it should return an array containing the result of applying each `fn` to the `args`.

Here's an example implementation of the `juxt` function:

```js
const juxt =
  (...fns) =>
  (...args) =>
    [...fns].map((fn) => [...args].map(fn));
```

Once you've defined the `juxt` function, you can use it by passing in any number of functions as arguments, followed by any number of arguments to pass to those functions.

Here are a couple examples of using the `juxt` function:

```js
juxt(
  (x) => x + 1,
  (x) => x - 1,
  (x) => x * 10
)(1, 2, 3); // [[2, 3, 4], [0, 1, 2], [10, 20, 30]]
```

```js
juxt(
  (s) => s.length,
  (s) => s.split(" ").join("-")
)("happy coding"); // [[18], ['happy-coding']]
```

In the first example, the `juxt` function takes three functions as arguments and returns a new function. When that new function is called with the arguments `1, 2, 3`, it applies each of the three functions to those arguments and returns an array of arrays containing the results.

In the second example, the `juxt` function takes two functions as arguments and returns a new function. When that new function is called with the argument `'happy-coding'`, it applies each of the two functions to that argument and returns an array of arrays containing the results.
