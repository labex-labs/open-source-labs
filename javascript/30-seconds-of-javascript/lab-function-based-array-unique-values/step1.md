# Finding Unique Values in an Array with a Function

To find all unique values of an array, provide a comparator function.

Use `Array.prototype.reduce()` and `Array.prototype.some()` to create an array containing only the first unique occurrence of each value. The comparator function `fn` takes two arguments, the values of the two elements being compared.

```js
const uniqueElementsBy = (arr, fn) =>
  arr.reduce((acc, v) => {
    if (!acc.some((x) => fn(v, x))) acc.push(v);
    return acc;
  }, []);
```

To test the function, use the example below:

```js
uniqueElementsBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" },
  ],
  (a, b) => a.id == b.id,
); // [ { id: 0, value: 'a' }, { id: 1, value: 'b' }, { id: 2, value: 'c' } ]
```

Start practicing coding by opening the Terminal/SSH and typing `node`.
