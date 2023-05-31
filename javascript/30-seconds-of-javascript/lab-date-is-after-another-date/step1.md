# How to Check if One Date is After Another Date in JavaScript

To check if one date comes after another date in JavaScript, you can use the greater than operator (`>`). Here's an example code snippet that checks if a given date (`dateA`) is after another date (`dateB`):

```js
const isAfterDate = (dateA, dateB) => dateA > dateB;
```

To use this function, simply pass in two date objects, like this:

```js
isAfterDate(new Date(2010, 10, 21), new Date(2010, 10, 20)); // true
```

To try this out, you can open the Terminal/SSH and type `node` to start practicing coding.
