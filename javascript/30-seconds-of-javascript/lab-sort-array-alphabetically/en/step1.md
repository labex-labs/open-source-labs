# How to Sort an Array Alphabetically Based on a Given Property in JavaScript

To sort an array of objects alphabetically based on a given property in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.sort()` to sort the array based on the given property.
3. Use `String.prototype.localeCompare()` to compare the values for the given property.

Here's an example code snippet that you can use:

```js
const alphabetical = (arr, getter, order = "asc") =>
  arr.sort(
    order === "desc"
      ? (a, b) => getter(b).localeCompare(getter(a))
      : (a, b) => getter(a).localeCompare(getter(b))
  );
```

You can call the `alphabetical` function with an array of objects and the getter function that returns the property to sort by. Here's an example usage:

```js
const people = [{ name: "John" }, { name: "Adam" }, { name: "Mary" }];
alphabetical(people, (g) => g.name);
// [ { name: 'Adam' }, { name: 'John' }, { name: 'Mary' } ]
alphabetical(people, (g) => g.name, "desc");
// [ { name: 'Mary' }, { name: 'John' }, { name: 'Adam' } ]
```
