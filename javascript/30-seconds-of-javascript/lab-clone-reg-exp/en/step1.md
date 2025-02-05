# Cloning a Regular Expression

To clone a regular expression, use the `RegExp` constructor, `RegExp.prototype.source`, and `RegExp.prototype.flags`.

```js
const cloneRegExp = (regExp) => new RegExp(regExp.source, regExp.flags);
```

This code will create a clone of the given regular expression. For example:

```js
const regExp = /lorem ipsum/gi;
const regExp2 = cloneRegExp(regExp); // regExp !== regExp2
```
