# NodeList to Array

> To start practicing coding, open the Terminal/SSH and type `node`.

Converts a `NodeList` to an array.

- Use spread operator (`...`) inside new array to convert a `NodeList` to an array.

```js
const nodeListToArray = nodeList => [...nodeList];
```

```js
nodeListToArray(document.childNodes); // [ <!DOCTYPE html>, html ]
```
