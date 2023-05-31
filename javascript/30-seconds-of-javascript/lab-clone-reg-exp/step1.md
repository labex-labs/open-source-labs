# Clone RegExp

> To start practicing coding, open the Terminal/SSH and type `node`.

Clones a regular expression.

- Use the `RegExp` constructor, `RegExp.prototype.source` and `RegExp.prototype.flags` to clone the given regular expression.

```js
const cloneRegExp = regExp => new RegExp(regExp.source, regExp.flags);
```

```js
const regExp = /lorem ipsum/gi;
const regExp2 = cloneRegExp(regExp); // regExp !== regExp2
```
