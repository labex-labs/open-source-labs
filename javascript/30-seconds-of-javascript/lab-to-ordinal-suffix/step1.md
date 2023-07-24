# Function to Convert Numbers to Ordinal Suffix

To convert a number to an ordinal suffix, use the `toOrdinalSuffix` function.

- Open the Terminal/SSH and type `node` to start practicing coding.
- The function takes a number as input and returns it as a string with the correct ordinal indicator suffix.
- Use the modulo operator (`%`) to find the values of the single and tens digits.
- Find which ordinal pattern digits match.
- If the digit is found in the teens pattern, use the teens ordinal.

```js
const toOrdinalSuffix = (num) => {
  const int = parseInt(num),
    digits = [int % 10, int % 100],
    ordinals = ["st", "nd", "rd", "th"],
    oPattern = [1, 2, 3, 4],
    tPattern = [11, 12, 13, 14, 15, 16, 17, 18, 19];
  return oPattern.includes(digits[0]) && !tPattern.includes(digits[1])
    ? int + ordinals[digits[0] - 1]
    : int + ordinals[3];
};
```

Here is an example of using the `toOrdinalSuffix` function:

```js
toOrdinalSuffix("123"); // '123rd'
```
