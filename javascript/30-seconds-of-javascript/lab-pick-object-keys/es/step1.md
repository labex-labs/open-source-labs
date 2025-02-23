# Instrucciones para elegir claves de objeto

Para elegir pares clave-valor específicos de un objeto, utiliza la función `pick(obj, arr)`.

- Pasa el objeto como primer argumento y una matriz de claves a elegir como segundo argumento.
- La función devuelve un nuevo objeto con solo los pares clave-valor que corresponden a las claves dadas.

Aquí hay un ejemplo de cómo usar `pick()`:

```js
const pick = (obj, arr) =>
  arr.reduce((acc, curr) => (curr in obj && (acc[curr] = obj[curr]), acc), {});

pick({ a: 1, b: "2", c: 3 }, ["a", "c"]); // { 'a': 1, 'c': 3 }
```

Para comenzar con la práctica de codificación, abre la Terminal/SSH y escribe `node`.
