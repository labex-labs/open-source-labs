# Código de la fábrica de coalescencia de argumentos

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`. Esta función devuelve el primer argumento que evalúa a `true` según el validador pasado como argumento.

```js
const coalesceFactory =
  (validator) =>
  (...args) =>
    args.find(validator);
```

Utiliza `Array.prototype.find()` para devolver el primer argumento que devuelve `true` de la función de validación de argumentos proporcionada, `valid`. Por ejemplo,

```js
const customCoalesce = coalesceFactory(
  (v) => ![null, undefined, "", NaN].includes(v)
);
customCoalesce(undefined, null, NaN, "", "Waldo"); // 'Waldo'
```

Aquí, la función `coalesceFactory` se personaliza para crear la función `customCoalesce`. La función `customCoalesce` filtra `null`, `undefined`, `NaN` y cadenas vacías de los argumentos proporcionados y devuelve el primer argumento que no es filtrado. La salida de `customCoalesce(undefined, null, NaN, '', 'Waldo')` es `'Waldo'`.
