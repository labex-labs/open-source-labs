# Converting JSON to CSV

To convert an array of objects to a comma-separated values (CSV) string with specified columns, use the following function:

```js
const JSONtoCSV = (arr, columns, delimiter = ",") =>
  [
    columns.join(delimiter),
    ...arr.map((obj) =>
      columns.reduce(
        (acc, key) =>
          `${acc}${!acc.length ? "" : delimiter}"${!obj[key] ? "" : obj[key]}"`,
        "",
      ),
    ),
  ].join("\n");
```

To use it, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Call the `JSONtoCSV` function with the following arguments:
   - `arr`: an array of objects to be converted.
   - `columns`: an array of strings that specify the columns to be included in the CSV output.
   - `delimiter`: an optional string that specifies the delimiter to be used (default value is `','`).
3. The function will return a CSV string that contains only the specified columns and the objects' values.
4. If no delimiter is specified, the default delimiter `','` will be used.
5. Examples of how to use the function are provided in the code block below.

```js
JSONtoCSV(
  [{ a: 1, b: 2 }, { a: 3, b: 4, c: 5 }, { a: 6 }, { b: 7 }],
  ["a", "b"],
); // 'a,b\n"1","2"\n"3","4"\n"6",""\n"","7"'

JSONtoCSV(
  [{ a: 1, b: 2 }, { a: 3, b: 4, c: 5 }, { a: 6 }, { b: 7 }],
  ["a", "b"],
  ";",
); // 'a;b\n"1";"2"\n"3";"4"\n"6";""\n"";"7"'
```
