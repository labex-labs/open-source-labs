# Una función que obtiene el n-ésimo argumento

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`. Aquí te mostramos cómo crear una función que obtiene el argumento en el índice `n`.

- Utiliza `Array.prototype.slice()` para obtener el argumento deseado en el índice `n`.
- Si `n` es negativo, se devuelve el n-ésimo argumento contando desde el final.

```js
const nthArg =
  (n) =>
  (...args) =>
    args.slice(n)[0];
```

Aquí te mostramos un ejemplo de cómo utilizar la función `nthArg`:

```js
const third = nthArg(2);
console.log(third(1, 2, 3)); // Salida: 3
console.log(third(1, 2)); // Salida: undefined

const last = nthArg(-1);
console.log(last(1, 2, 3, 4, 5)); // Salida: 5
```
