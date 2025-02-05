# Converting Integer to Roman Numeral

To convert an integer to its roman numeral representation, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.

2. The function `toRomanNumeral()` accepts values between `1` and `3999` (both inclusive).

3. Create a lookup table containing 2-value arrays in the form of (roman value, integer).

4. Use `Array.prototype.reduce()` to loop over the values in `lookup` and repeatedly divide `num` by the value.

5. Use `String.prototype.repeat()` to add the roman numeral representation to the accumulator.

Here is the code for the `toRomanNumeral()` function:

```js
const toRomanNumeral = (num) => {
  const lookup = [
    ["M", 1000],
    ["CM", 900],
    ["D", 500],
    ["CD", 400],
    ["C", 100],
    ["XC", 90],
    ["L", 50],
    ["XL", 40],
    ["X", 10],
    ["IX", 9],
    ["V", 5],
    ["IV", 4],
    ["I", 1]
  ];
  return lookup.reduce((acc, [k, v]) => {
    acc += k.repeat(Math.floor(num / v));
    num = num % v;
    return acc;
  }, "");
};
```

You can test the function with these examples:

```js
toRomanNumeral(3); // 'III'
toRomanNumeral(11); // 'XI'
toRomanNumeral(1998); // 'MCMXCVIII'
```
