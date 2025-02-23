# Comprobando si un valor es una función generadora

Para comprobar si un valor es una función generadora, puedes utilizar la función `isGeneratorFunction`. Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Aquí es cómo funciona la función `isGeneratorFunction`:

- Comprueba si el argumento dado es una función generadora utilizando `Object.prototype.toString()` y `Function.prototype.call()`.
- Si el resultado de la comprobación es `'[object GeneratorFunction]'`, entonces el valor es una función generadora.

Aquí está el código de la función `isGeneratorFunction`:

```js
const isGeneratorFunction = (val) =>
  Object.prototype.toString.call(val) === "[object GeneratorFunction]";
```

Y aquí hay algunos ejemplos de cómo usarlo:

```js
isGeneratorFunction(function () {}); // false
isGeneratorFunction(function* () {}); // true
```
