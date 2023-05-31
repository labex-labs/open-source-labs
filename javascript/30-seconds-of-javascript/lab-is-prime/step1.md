# Number Is Prime

> To start practicing coding, open the Terminal/SSH and type `node`.

Checks if the provided integer is a prime number.

- Check numbers from `2` to the square root of the given number.
- Return `false` if any of them divides the given number, else return `true`, unless the number is less than `2`.

```js
const isPrime = num => {
  const boundary = Math.floor(Math.sqrt(num));
  for (let i = 2; i <= boundary; i++) if (num % i === 0) return false;
  return num >= 2;
};
```

```js
isPrime(11); // true
```
