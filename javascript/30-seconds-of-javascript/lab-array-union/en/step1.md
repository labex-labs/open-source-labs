# How to Find the Union of Two Arrays in JavaScript

To find the union of two arrays in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.

2. The union of two arrays returns every element that exists in any of the two arrays at least once.

3. To get the union of two arrays, create a `Set` with all values of `a` and `b`, and convert it to an array using the `Array.from()` method.

Here's an example of how to implement this:

```js
const union = (a, b) => Array.from(new Set([...a, ...b]));

console.log(union([1, 2, 3], [4, 3, 2])); // Output: [1, 2, 3, 4]
```

In the example above, the `union()` function takes two arrays, `[1, 2, 3]` and `[4, 3, 2]`, as arguments and returns the union of the two arrays as an array `[1, 2, 3, 4]`.
