# Función para indexar una matriz

Para indexar una matriz usando una función, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `Array.prototype.reduce()` para crear un objeto a partir de la matriz.
3. Aplica la función proporcionada a cada valor de la matriz para producir una clave y agrega el par clave-valor al objeto.

Aquí hay un fragmento de código de ejemplo:

```js
const indexBy = (arr, fn) =>
  arr.reduce((obj, v, i) => {
    obj[fn(v, i, arr)] = v;
    return obj;
  }, {});
```

Puedes usar esta función de la siguiente manera:

```js
indexBy(
  [
    { id: 10, name: "apple" },
    { id: 20, name: "orange" }
  ],
  (x) => x.id
);
// { '10': { id: 10, name: 'apple' }, '20': { id: 20, name: 'orange' } }
```

Esta función crea un objeto a partir de una matriz mapeando cada valor a una clave usando una función proporcionada. El objeto resultante contiene pares clave-valor donde las claves son producidas por la función y los valores son los elementos originales de la matriz.
