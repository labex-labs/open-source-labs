# Function to Calculate Sum of Powers in a Given Range

To calculate the sum of the powers of all the numbers within a specified range (including both endpoints), use the following function:

```js
const sumPower = (end, power = 2, start = 1) =>
  Array(end + 1 - start)
    .fill(0)
    .map((x, i) => (i + start) ** power)
    .reduce((a, b) => a + b, 0);
```

Here's how you can use this function:

- Call `sumPower(end)` to calculate the sum of squares of all numbers from 1 to `end`.
- Call `sumPower(end, power)` to calculate the sum of `power`th powers of all numbers from 1 to `end`.
- Call `sumPower(end, power, start)` to calculate the sum of `power`th powers of all numbers from `start` to `end`.

Note that the second and third arguments (`power` and `start`) are optional, and default to `2` and `1` respectively if not provided.

Example:

```js
sumPower(10); // Returns 385 (sum of squares of numbers from 1 to 10)
sumPower(10, 3); // Returns 3025 (sum of cubes of numbers from 1 to 10)
sumPower(10, 3, 5); // Returns 2925 (sum of cubes of numbers from 5 to 10)
```
