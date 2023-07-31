# Converting a String from Camelcase

To convert a string from camelcase, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `String.prototype.replace()` method to break the string into words and add a `separator` between them.
3. If you don't provide a `separator`, the default `_` separator will be used.
4. The `fromCamelCase` function takes two arguments: `str` (the string to convert) and `separator` (the separator to use).
5. The function uses two regular expressions to insert the separator between words.
6. The first regular expression matches a lowercase letter or digit followed by an uppercase letter and inserts the separator between them.
7. The second regular expression matches a sequence of uppercase letters followed by a sequence of uppercase letters and digits and inserts the separator between them.
8. The function then converts the resulting string to lowercase.
9. To convert a string from camelcase, call the `fromCamelCase` function and pass in the string and the separator (if you want to use a custom separator).
10. Examples:

```js
fromCamelCase("someDatabaseFieldName", " "); // 'some database field name'
fromCamelCase("someLabelThatNeedsToBeDecamelized", "-");
// 'some-label-that-needs-to-be-decamelized'
fromCamelCase("someJavascriptProperty", "_"); // 'some_javascript_property'
fromCamelCase("JSONToCSV", "."); // 'json.to.csv'
```
