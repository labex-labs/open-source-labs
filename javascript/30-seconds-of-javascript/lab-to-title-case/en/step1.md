# Function to Convert String to Title Case

To convert a given string to title case, use the following function. It uses `String.prototype.match()` to break the string into words using an appropriate regular expression. Then it combines them using `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()`, and `String.prototype.toUpperCase()`. This capitalizes the first letter of each word and adds a whitespace between them.

```js
const toTitleCase = (str) =>
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
```

Here are some examples of how to use the function:

```js
toTitleCase("some_database_field_name"); // 'Some Database Field Name'
toTitleCase("Some label that needs to be title-cased");
// 'Some Label That Needs To Be Title Cased'
toTitleCase("some-package-name"); // 'Some Package Name'
toTitleCase("some-mixed_string with spaces_underscores-and-hyphens");
// 'Some Mixed String With Spaces Underscores And Hyphens'
```
