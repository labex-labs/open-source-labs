# How to Order an Array of Objects in JavaScript

To order an array of objects in JavaScript, you can use the `Array.prototype.sort()` method and `Array.prototype.reduce()` method on the `props` array with a default value of `0`.

Here's an example function, `orderBy`, that sorts an array of objects based on the specified properties and orders:

```js
const orderBy = (arr, props, orders = ["asc"]) =>
  [...arr].sort((a, b) =>
    props.reduce((acc, prop, i) => {
      if (acc === 0) {
        const [p1, p2] =
          orders[i] === "desc" ? [b[prop], a[prop]] : [a[prop], b[prop]];
        acc = p1 > p2 ? 1 : p1 < p2 ? -1 : 0;
      }
      return acc;
    }, 0)
  );
```

To use this function, pass in an array of objects, an array of properties to sort by, and an optional array of orders. If no `orders` array is supplied, the function will sort by `'asc'` by default.

Here are some examples of how to use the `orderBy` function:

```js
const users = [
  { name: "fred", age: 48 },
  { name: "barney", age: 36 },
  { name: "fred", age: 40 }
];

// sort by name ascending and age descending
orderBy(users, ["name", "age"], ["asc", "desc"]);
// Output: [{name: 'barney', age: 36}, {name: 'fred', age: 48}, {name: 'fred', age: 40}]

// sort by name ascending and age ascending (default order)
orderBy(users, ["name", "age"]);
// Output: [{name: 'barney', age: 36}, {name: 'fred', age: 40}, {name: 'fred', age: 48}]
```
