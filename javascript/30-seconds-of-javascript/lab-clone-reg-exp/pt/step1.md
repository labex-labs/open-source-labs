# Clonando uma Expressão Regular

Para clonar uma expressão regular, use o construtor `RegExp`, `RegExp.prototype.source` e `RegExp.prototype.flags`.

```js
const cloneRegExp = (regExp) => new RegExp(regExp.source, regExp.flags);
```

Este código criará um clone da expressão regular fornecida. Por exemplo:

```js
const regExp = /lorem ipsum/gi;
const regExp2 = cloneRegExp(regExp); // regExp !== regExp2
```
