# How to Group and Count Elements in an Array Using JavaScript

To group and count elements in an array using JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Array.prototype.map()` method to map the values of an array to a function or property name.
3. Use the `Array.prototype.reduce()` method to create an object where the keys are produced from the mapped results.
4. Create a function called `countBy` that takes an array and a function as arguments.
5. Inside the `countBy` function, use a ternary operator to check if the argument passed is a function or a property name. If it's a function, use it as the mapping function. If it's a property name, access that property of the array elements.
6. Use the `reduce()` method to create an object where each key represents a unique element in the array and its value is the number of times it appears in the array.

Here's the code:

```js
const countBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => {
      acc[val] = (acc[val] || 0) + 1;
      return acc;
    }, {});
```

You can test the `countBy` function with the following examples:

```js
countBy([6.1, 4.2, 6.3], Math.floor); // {4: 1, 6: 2}
countBy(["one", "two", "three"], "length"); // {3: 2, 5: 1}
countBy([{ count: 5 }, { count: 10 }, { count: 5 }], (x) => x.count); // {5: 2, 10: 1}
```
