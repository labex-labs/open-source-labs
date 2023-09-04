# Function to Find Reversed Unique Values in Array

To find all the unique values of an array based on a provided comparator function from the right, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.reduceRight()` and `Array.prototype.some()` to create an array containing only the last unique occurrence of each value, based on the comparator function `fn`.
3. The comparator function takes two arguments: the values of the two elements being compared.
4. Here's the code to implement the function:

```js
const uniqueElementsByRight = (arr, fn) =>
  arr.reduceRight((acc, v) => {
    if (!acc.some((x) => fn(v, x))) acc.push(v);
    return acc;
  }, []);
```

5. Use the following code to test the function:

```js
uniqueElementsByRight(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" },
  ],
  (a, b) => a.id == b.id,
); // [ { id: 0, value: 'e' }, { id: 1, value: 'd' }, { id: 2, value: 'c' } ]
```
