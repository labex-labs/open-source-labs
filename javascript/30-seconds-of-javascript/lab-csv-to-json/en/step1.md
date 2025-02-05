# CSV to JSON

To convert a comma-separated values (CSV) string to a 2D array of objects and use it to practice coding, open the Terminal/SSH and type `node`. The first row of the string is used as the title row. Here are the steps to convert CSV to JSON:

1. Use `Array.prototype.indexOf()` to find the first newline character (`\n`).
2. Use `Array.prototype.slice()` to remove the first row (title row) and `String.prototype.split()` to separate it into values, using the provided `delimiter`.
3. Use `String.prototype.split()` to create a string for each row.
4. Use `String.prototype.split()` to separate the values in each row, using the provided `delimiter`.
5. Use `Array.prototype.reduce()` to create an object for each row's values, with the keys parsed from the title row.
6. Omit the second argument, `delimiter`, to use a default delimiter of `,`.

Here's the code:

```js
const CSVToJSON = (data, delimiter = ",") => {
  const titles = data.slice(0, data.indexOf("\n")).split(delimiter);
  return data
    .slice(data.indexOf("\n") + 1)
    .split("\n")
    .map((v) => {
      const values = v.split(delimiter);
      return titles.reduce(
        (obj, title, index) => ((obj[title] = values[index]), obj),
        {}
      );
    });
};
```

To test the function, use the following examples:

```js
CSVToJSON("col1,col2\na,b\nc,d");
// [{'col1': 'a', 'col2': 'b'}, {'col1': 'c', 'col2': 'd'}];
CSVToJSON("col1;col2\na;b\nc;d", ";");
// [{'col1': 'a', 'col2': 'b'}, {'col1': 'c', 'col2': 'd'}];
```
