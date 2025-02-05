# How to Find the Minimum Date in JavaScript

To find the minimum date value in JavaScript, you can use the ES6 spread syntax with `Math.min()` and the `Date` constructor. Here's an example code snippet:

```js
const minDate = (...dates) => new Date(Math.min(...dates));
```

To use this function, create an array of `Date` objects and pass it to `minDate()` using the spread syntax. Here's an example:

```js
const dates = [
  new Date(2017, 4, 13),
  new Date(2018, 2, 12),
  new Date(2016, 0, 10),
  new Date(2016, 0, 9)
];
minDate(...dates); // Returns a `Date` object representing 2016-01-08T22:00:00.000Z
```

By using this code, you can easily find the minimum date value in JavaScript.
