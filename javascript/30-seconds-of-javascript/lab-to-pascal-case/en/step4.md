# Creating the Complete toPascalCase Function

Now that we understand all the components needed, let's create a complete `toPascalCase` function that can handle any input string.

1. Let's create a JavaScript file to save our function. Exit your Node.js session by pressing Ctrl+C twice or typing `.exit`.

2. In the WebIDE, create a new file by clicking "File" > "New File" in the top menu.

3. Save the file as `pascalCase.js` in the `/home/labex/project` directory.

4. Copy and paste the following code into the editor:

```javascript
/**
 * Converts a string to Pascal case.
 * @param {string} str - The input string to convert.
 * @returns {string} The Pascal cased string.
 */
function toPascalCase(str) {
  // Use regex to match words regardless of delimiter
  const words = str.match(
    /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g
  );

  // If no words are found, return an empty string
  if (!words) {
    return "";
  }

  // Capitalize each word and join them
  return words
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join("");
}

// Test cases
console.log(toPascalCase("hello world")); // "HelloWorld"
console.log(toPascalCase("some_database_field_name")); // "SomeDatabaseFieldName"
console.log(toPascalCase("Some label that needs to be pascalized")); // "SomeLabelThatNeedsToBePascalized"
console.log(toPascalCase("some-javascript-property")); // "SomeJavascriptProperty"
console.log(
  toPascalCase("some-mixed_string with spaces_underscores-and-hyphens")
); // "SomeMixedStringWithSpacesUnderscoresAndHyphens"
```

5. Save the file by pressing Ctrl+S or selecting "File" > "Save" from the menu.

6. Run the file using Node.js by opening the Terminal and typing:

```bash
node pascalCase.js
```

You should see the following output:

```
HelloWorld
SomeDatabaseFieldName
SomeLabelThatNeedsToBePascalized
SomeJavascriptProperty
SomeMixedStringWithSpacesUnderscoresAndHyphens
```

Our `toPascalCase` function is now working correctly. Let's review how it works:

1. We use a regular expression to match words in the input string, regardless of the delimiters used.
2. We check if any words were found. If not, we return an empty string.
3. We use `map()` to capitalize each word and `join('')` to combine them without separators.
4. The result is a Pascal-cased string where each word begins with an uppercase letter and the rest are lowercase.
