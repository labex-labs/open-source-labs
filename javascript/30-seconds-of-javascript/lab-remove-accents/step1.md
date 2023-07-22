# Remove Accents

This function removes accents from strings.

- Use `String.prototype.normalize()` to convert the string to a normalized Unicode format.
- Use `String.prototype.replace()` to replace diacritical marks in the given Unicode range with empty strings.

```js
const removeAccents = (str) =>
  str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
```

To use this function, open the Terminal/SSH and type `node`. Then, call the function with a string as its argument.

```js
removeAccents("Antoine de Saint-Exupéry"); // 'Antoine de Saint-Exupery'
```
