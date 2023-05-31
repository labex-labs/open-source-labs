# Converting NodeList to Array

To convert a `NodeList` to an array, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the spread operator (`...`) inside a new array to convert the `NodeList`.
3. Create a function called `nodeListToArray` that takes a `NodeList` as its argument and returns an array using the spread operator.
4. Call the function with the `NodeList` you want to convert as the argument.

Here's an example:

```js
const nodeListToArray = (nodeList) => [...nodeList];

nodeListToArray(document.childNodes); // [ <!DOCTYPE html>, html ]
```

By following these steps, you can easily convert a `NodeList` to an array in your code.
