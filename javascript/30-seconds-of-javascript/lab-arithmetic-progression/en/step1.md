# Arithmetic Progression Code Example

To practice coding, open the Terminal/SSH and type `node`.

Here is an example code that creates an array of numbers in arithmetic progression. The array starts with a given positive integer and goes up to a specified limit:

```js
const arithmeticProgression = (n, lim) =>
  Array.from({ length: Math.ceil(lim / n) }, (_, i) => (i + 1) * n);
```

To use this code, simply call the function `arithmeticProgression` with two arguments: the starting positive integer and the limit. For example:

```js
arithmeticProgression(5, 25); // [5, 10, 15, 20, 25]
```
