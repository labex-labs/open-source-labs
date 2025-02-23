# Clonar una Expresión Regular

Para clonar una expresión regular, utiliza el constructor `RegExp`, `RegExp.prototype.source` y `RegExp.prototype.flags`.

```js
const cloneRegExp = (regExp) => new RegExp(regExp.source, regExp.flags);
```

Este código creará una copia de la expresión regular dada. Por ejemplo:

```js
const regExp = /lorem ipsum/gi;
const regExp2 = cloneRegExp(regExp); // regExp!== regExp2
```
