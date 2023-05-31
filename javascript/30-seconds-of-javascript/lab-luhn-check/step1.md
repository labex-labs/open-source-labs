# Luhn Check

To use the Luhn Algorithm for validation of identification numbers, such as credit card numbers, IMEI numbers, National Provider Identifier numbers, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the following methods: `String.prototype.split()`, `Array.prototype.reverse()`, `Array.prototype.map()`, and `parseInt()` in combination to obtain an array of digits.
3. Use `Array.prototype.shift()` to obtain the last digit.
4. Use `Array.prototype.reduce()` to implement the Luhn Algorithm.
5. Return `true` if `sum` is divisible by `10`, `false` otherwise.

Here's the code:

```js
const luhnCheck = (num) => {
  const arr = (num + "")
    .split("")
    .reverse()
    .map((x) => parseInt(x));
  const lastDigit = arr.shift();
  let sum = arr.reduce(
    (acc, val, i) =>
      i % 2 !== 0 ? acc + val : acc + ((val *= 2) > 9 ? val - 9 : val),
    0
  );
  sum += lastDigit;
  return sum % 10 === 0;
};
```

You can test the Luhn Check function using these examples:

```js
luhnCheck("4485275742308327"); // true
luhnCheck(6011329933655299); //  true
luhnCheck(123456789); // false
```
