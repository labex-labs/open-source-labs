# Generating Primes Using Sieve of Eratosthenes

To generate primes up to a given number using the Sieve of Eratosthenes, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Create an array containing numbers from `2` to the given number.
3. Use `Array.prototype.filter()` to filter out the values that are divisible by any number from `2` to the square root of the provided number.
4. Return the resulting array containing primes.

Here's the JavaScript code to generate primes up to a given number:

```js
const generatePrimes = (num) => {
  let arr = Array.from({ length: num - 1 }).map((x, i) => i + 2),
    sqrt = Math.floor(Math.sqrt(num)),
    numsTillSqrt = Array.from({ length: sqrt - 1 }).map((x, i) => i + 2);
  numsTillSqrt.forEach(
    (x) => (arr = arr.filter((y) => y % x !== 0 || y === x)),
  );
  return arr;
};
```

You can call the function `generatePrimes()` by passing the desired number as an argument. For example:

```js
generatePrimes(10); // [2, 3, 5, 7]
```
