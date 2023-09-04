# Camelcase String Conversion

To convert a string to camelcase, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `String.prototype.match()` with an appropriate regular expression to break the string into words.
3. Use `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()`, `String.prototype.toLowerCase()`, and `String.prototype.toUpperCase()` to combine the words and capitalize the first letter of each one.
4. Use the `toCamelCase` function shown below to perform the conversion:

```js
const toCamelCase = (str) => {
  const words =
    str &&
    str.match(
      /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g,
    );
  const capitalizedWords =
    words &&
    words.map(
      (word) => word.slice(0, 1).toUpperCase() + word.slice(1).toLowerCase(),
    );
  const camelCaseString = capitalizedWords && capitalizedWords.join("");
  return (
    camelCaseString &&
    camelCaseString.slice(0, 1).toLowerCase() + camelCaseString.slice(1)
  );
};
```

Here are some examples of how to use the `toCamelCase` function:

```js
toCamelCase("some_database_field_name"); // 'someDatabaseFieldName'
toCamelCase("Some label that needs to be camelized");
// 'someLabelThatNeedsToBeCamelized'
toCamelCase("some-javascript-property"); // 'someJavascriptProperty'
toCamelCase("some-mixed_string with spaces_underscores-and-hyphens");
// 'someMixedStringWithSpacesUnderscoresAndHyphens'
```
