# How to Find Array Intersection Based on Function using JavaScript

To find the elements that exist in both arrays based on a provided comparator function, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.

2. Use `Array.prototype.filter()` and `Array.prototype.findIndex()` in combination with the provided comparator to determine intersecting values.

   ```js
   const intersectionWith = (a, b, comp) =>
     a.filter((x) => b.findIndex((y) => comp(x, y)) !== -1);
   ```

3. Call the `intersectionWith()` function with the two arrays and the comparator function as arguments.

   ```js
   intersectionWith(
     [1, 1.2, 1.5, 3, 0],
     [1.9, 3, 0, 3.9],
     (a, b) => Math.round(a) === Math.round(b),
   ); // [1.5, 3, 0]
   ```

This will return an array containing the intersecting values between the two arrays, based on the provided comparator function.
