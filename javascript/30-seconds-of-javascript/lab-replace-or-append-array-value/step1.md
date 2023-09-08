# How to Replace or Append Array Value

To replace an item in an array or append it if it doesn't exist, follow these steps:

1. Use the spread operator (`...`) to create a shallow copy of the array.
2. Use `Array.prototype.findIndex()` to find the index of the first element that satisfies the provided comparison function `compFn`.
3. If no such element is found, use `Array.prototype.push()` to append the new value to the array.
4. Otherwise, use `Array.prototype.splice()` to replace the value at the found index with the new value.

Here is an example of how to implement this functionality:

```js
const replaceOrAppend = (arr, val, compFn) => {
  const res = [...arr];
  const i = arr.findIndex((v) => compFn(v, val));
  if (i === -1) res.push(val);
  else res.splice(i, 1, val);
  return res;
};
```

You can use this function with an array of objects like this:

```js
const people = [
  { name: "John", age: 30 },
  { name: "Jane", age: 28 }
];
const jane = { name: "Jane", age: 29 };
const jack = { name: "Jack", age: 28 };
replaceOrAppend(people, jane, (a, b) => a.name === b.name);
// [ { name: 'John', age: 30 }, { name: 'Jane', age: 29 } ]
replaceOrAppend(people, jack, (a, b) => a.name === b.name);
// [
//   { name: 'John', age: 30 },
//   { name: 'Jane', age: 28 },
//   { name: 'Jack', age: 28 }
// ]
```
