# Finding the Maximum Date

To find the maximum date value from a given array of dates, follow these steps:

1. Open the Terminal or SSH.
2. Type `node` to start practicing coding.
3. Use the ES6 spread syntax with `Math.max()` to find the maximum date value.
4. Convert the maximum date value to a `Date` object using the `Date` constructor.

Here's an example code snippet:

```js
const maxDate = (...dates) => new Date(Math.max(...dates));

const dates = [
  new Date(2017, 4, 13),
  new Date(2018, 2, 12),
  new Date(2016, 0, 10),
  new Date(2016, 0, 9)
];

maxDate(...dates); // Returns "2018-03-11T22:00:00.000Z"
```

By following these steps and using the provided code, you can easily find the maximum date value from a given array of dates.
