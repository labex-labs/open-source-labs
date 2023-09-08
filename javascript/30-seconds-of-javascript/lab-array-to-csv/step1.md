# Convert 2D Array to CSV

To convert a 2D array to a comma-separated values (CSV) string, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.map()` and `Array.prototype.join()` to combine individual 1D arrays (rows) into strings, using the provided `delimiter`.
3. Use `Array.prototype.join()` to combine all rows into a CSV string, separating each row with a newline (`\n`).
4. If you want to use the default delimiter of `,`, omit the second argument, `delimiter`.

Here is an example of the code:

```js
const arrayToCSV = (arr, delimiter = ",") =>
  arr
    .map((v) =>
      v
        .map((x) => (isNaN(x) ? `"${x.replace(/"/g, '""')}"` : x))
        .join(delimiter)
    )
    .join("\n");
```

You can test the function by running the following lines of code:

```js
arrayToCSV([
  ["a", "b"],
  ["c", "d"]
]); // '"a","b"\n"c","d"'
arrayToCSV(
  [
    ["a", "b"],
    ["c", "d"]
  ],
  ";"
); // '"a";"b"\n"c";"d"'
arrayToCSV([
  ["a", '"b" great'],
  ["c", 3.1415]
]);
// '"a","""b"" great"\n"c",3.1415'
```
