# How to Order an Array of Objects Based on Property Order

To order an array of objects based on a property order, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.reduce()` to create an object from the `order` array with the values as keys and their original index as the value.
3. Use `Array.prototype.sort()` to sort the given array, skipping elements for which `prop` is empty or not in the `order` array.

Here's an example code snippet for ordering an array of objects based on a property order:

```js
const orderWith = (arr, prop, order) => {
  const orderValues = order.reduce((acc, v, i) => {
    acc[v] = i;
    return acc;
  }, {});
  return [...arr].sort((a, b) => {
    if (orderValues[a[prop]] === undefined) return 1;
    if (orderValues[b[prop]] === undefined) return -1;
    return orderValues[a[prop]] - orderValues[b[prop]];
  });
};
```

You can use the `orderWith` function to order an array of objects based on a property order. For example:

```js
const users = [
  { name: "fred", language: "Javascript" },
  { name: "barney", language: "TypeScript" },
  { name: "frannie", language: "Javascript" },
  { name: "anna", language: "Java" },
  { name: "jimmy" },
  { name: "nicky", language: "Python" },
];
orderWith(users, "language", ["Javascript", "TypeScript", "Java"]);
/*
[
  { name: 'fred', language: 'Javascript' },
  { name: 'frannie', language: 'Javascript' },
  { name: 'barney', language: 'TypeScript' },
  { name: 'anna', language: 'Java' },
  { name: 'jimmy' },
  { name: 'nicky', language: 'Python' }
]
*/
```
