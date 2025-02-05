# Function to check if a number is prime

To practice coding, open the Terminal/SSH and type `node`. This function checks if a given integer is a prime number. Here are the steps to check if a number is prime:

1. Check numbers from `2` to the square root of the given number.
2. If any of them divides the given number, return `false`.
3. If none of them divides the given number, return `true`, unless the number is less than `2`.

Here's the code to implement this function in JavaScript:

```js
const isPrime = (num) => {
  const boundary = Math.floor(Math.sqrt(num));
  for (let i = 2; i <= boundary; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return num >= 2;
};
```

You can test the function by calling it with a number as an argument:

```js
isPrime(11); // true
```
