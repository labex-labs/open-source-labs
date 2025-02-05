# Converting CSV to an Array

To convert a comma-separated values (CSV) string to a 2D array, follow these steps:

1. Open the Terminal/SSH and type `node` to start coding.
2. Use `Array.prototype.indexOf()` to locate the first newline character (`\n`).
3. Use `Array.prototype.slice()` to remove the first row (title row) if `omitFirstRow` is set to `true`.
4. Use `String.prototype.split()` to create a string for each row.
5. Use `String.prototype.split()` to separate the values in each row using the provided `delimiter`.
6. If you don't provide the second argument, `delimiter`, the default delimiter of `','` will be used.
7. If you don't provide the third argument, `omitFirstRow`, the first row (title row) of the CSV string will be included.

Here's the code to convert CSV to an array:

```js
const CSVToArray = (data, delimiter = ",", omitFirstRow = false) =>
  data
    .slice(omitFirstRow ? data.indexOf("\n") + 1 : 0)
    .split("\n")
    .map((v) => v.split(delimiter));
```

You can use the following examples to test the function:

```js
CSVToArray("a,b\nc,d"); // [['a', 'b'], ['c', 'd']];
CSVToArray("a;b\nc;d", ";"); // [['a', 'b'], ['c', 'd']];
CSVToArray("col1,col2\na,b\nc,d", ",", true); // [['a', 'b'], ['c', 'd']];
```
