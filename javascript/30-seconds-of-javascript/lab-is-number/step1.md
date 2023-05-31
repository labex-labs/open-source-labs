# Checking if a Value is a Number in JavaScript

To check if a value is a number in JavaScript, you can use the `typeof` operator to determine if the value is classified as a number primitive. To prevent issues with `NaN`, which has a `typeof` equal to `number` and is not equal to itself, you can also check if the value is equal to itself using `val === val`.

Here's an example function that checks if a given value is a number:

```js
const isNumber = (val) => typeof val === "number" && val === val;
```

You can use this function like so:

```js
isNumber(1); // true
isNumber("1"); // false
isNumber(NaN); // false
```
