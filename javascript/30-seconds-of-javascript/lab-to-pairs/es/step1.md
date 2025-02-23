# Convertir un objeto en pares

Para convertir un objeto en una matriz de pares clave-valor, utiliza la función `toPairs`. Para comenzar a codificar, abre la Terminal/SSH y escribe `node`.

La función `toPairs` funciona de la siguiente manera:

- Primero, verifica si `Symbol.iterator` está definido para el objeto iterable dado.
- Si `Symbol.iterator` está definido, utiliza `Array.prototype.entries()` para obtener un iterador para el objeto y luego convierte el resultado en una matriz de matrices de pares clave-valor utilizando `Array.from()`.
- Si `Symbol.iterator` no está definido para el objeto, utiliza `Object.entries()` en su lugar.

Aquí está el código para la función `toPairs`:

```js
const toPairs = (obj) =>
  obj[Symbol.iterator] instanceof Function && obj.entries instanceof Function
    ? Array.from(obj.entries())
    : Object.entries(obj);
```

Puedes utilizar la función `toPairs` con varios tipos de objetos, como:

```js
toPairs({ a: 1, b: 2 }); // [['a', 1], ['b', 2]]
toPairs([2, 4, 8]); // [[0, 2], [1, 4], [2, 8]]
toPairs("shy"); // [['0','s'], ['1', 'h'], ['2', 'y']]
toPairs(new Set(["a", "b", "c", "a"])); // [['a', 'a'], ['b', 'b'], ['c', 'c']]
```
