# How to Check if One Date is Before Another in JavaScript

To check if one date comes before another in JavaScript, you can use the less than operator (`<`). Here's an example function that takes in two dates and returns a boolean value indicating whether the first date comes before the second:

```js
const isBeforeDate = (dateA, dateB) => dateA < dateB;
```

You can use this function to check if a specific date comes before another date by passing in two `Date` objects as arguments. For example:

```js
isBeforeDate(new Date(2010, 10, 20), new Date(2010, 10, 21)); // true
```
