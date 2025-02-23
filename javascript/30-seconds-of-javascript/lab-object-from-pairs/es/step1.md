# Crear un objeto a partir de pares de clave-valor

Para crear un objeto a partir de pares de clave-valor, utiliza la función `objectFromPairs`.

- Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
- La función utiliza `Array.prototype.reduce()` para crear y combinar pares de clave-valor.
- Para una implementación más simple, también puedes utilizar [`Object.fromEntries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries).

```js
const objectFromPairs = (arr) =>
  arr.reduce((a, [key, val]) => ((a[key] = val), a), {});
```

Uso de ejemplo:

```js
objectFromPairs([
  ["a", 1],
  ["b", 2]
]); // {a: 1, b: 2}
```
