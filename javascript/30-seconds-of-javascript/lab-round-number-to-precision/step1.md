# Here's how to round a number to a given precision in JavaScript:

```
const round = (n, decimals = 0) =>
  Number(`${Math.round(`${n}e${decimals}`)}e-${decimals}`);
```

- Use `Math.round()` and template literals to round the number to the specified number of digits.
- If you want to round to an integer, omit the second argument, `decimals`.
- To start practicing coding, open the Terminal/SSH and type `node`.
- For example, `round(1.005, 2)` will return `1.01`.
