# Function to Convert String to Pascal Case

To convert a string to Pascal case, you can use the `toPascalCase()` function. Here's how:

- First, open the Terminal/SSH and type `node` to start practicing coding.
- Then, use the `String.prototype.match()` method with an appropriate regular expression to break the string into words.
- Next, use the `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()`, `String.prototype.toUpperCase()`, and `String.prototype.toLowerCase()` methods to combine the words, capitalizing the first letter of each word and lowercasing the rest.
- Finally, call the `toPascalCase()` function with your desired string as an argument to convert it to Pascal case.

Here's the code for the `toPascalCase()` function:

```js
const toPascalCase = (str) =>
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((x) => x.charAt(0).toUpperCase() + x.slice(1).toLowerCase())
    .join("");
```

You can use this function to convert any string to Pascal case. Here are some examples:

```js
toPascalCase("some_database_field_name"); // 'SomeDatabaseFieldName'
toPascalCase("Some label that needs to be pascalized"); // 'SomeLabelThatNeedsToBePascalized'
toPascalCase("some-javascript-property"); // 'SomeJavascriptProperty'
toPascalCase("some-mixed_string with spaces_underscores-and-hyphens"); // 'SomeMixedStringWithSpacesUnderscoresAndHyphens'
```
