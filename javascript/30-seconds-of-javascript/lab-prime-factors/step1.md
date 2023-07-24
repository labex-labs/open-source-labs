# How to Find Prime Factors of a Number using Trial Division Algorithm

To find prime factors of a given number using trial division algorithm, follow these steps:

- Open the Terminal/SSH and type `node` to start practicing coding.
- Use a `while` loop to iterate over all possible prime factors, starting with `2`.
- If the current factor, `f`, exactly divides `n`, add `f` to the factors array and divide `n` by `f`. Otherwise, increment `f` by one.
- The function `primeFactors` takes a number `n` as input and returns an array of its prime factors.
- To test the function, call `primeFactors(147)` and it will return `[3, 7, 7]`.

Here's the JavaScript code:

```js
const primeFactors = (n) => {
  let a = [],
    f = 2;
  while (n > 1) {
    if (n % f === 0) {
      a.push(f);
      n /= f;
    } else {
      f++;
    }
  }
  return a;
};
```

Remember to replace `147` with the number you want to find prime factors of.
