# Javascript Function to Decapitalize String

To decapitalize the first letter of a string, use the following JavaScript function:

```js
const decapitalize = ([first, ...rest], upperRest = false) => {
  return (
    first.toLowerCase() +
    (upperRest ? rest.join("").toUpperCase() : rest.join(""))
  );
};
```

To use this function, open the Terminal/SSH and type `node`. Then, call the `decapitalize` function, passing in the string you want to decapitalize as the first argument.

Optionally, you can set the second argument `upperRest` to `true` to convert the rest of the string to uppercase. If `upperRest` is not provided, it defaults to `false`.

Here are some examples:

```js
decapitalize("FooBar"); // 'fooBar'
decapitalize("FooBar", true); // 'fOOBAR'
```
