# Cómo particionar un arreglo en dos basado en una función

Para particionar un arreglo en dos basado en una función dada, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `Array.prototype.reduce()` para crear un arreglo de dos arreglos.
3. Utiliza `Array.prototype.push()` para agregar los elementos para los cuales `fn` devuelve `true` al primer arreglo y los elementos para los cuales `fn` devuelve `false` al segundo.

Aquí está el código que puedes utilizar:

```js
const partition = (arr, fn) =>
  arr.reduce(
    (acc, val, i, arr) => {
      acc[fn(val, i, arr) ? 0 : 1].push(val);
      return acc;
    },
    [[], []]
  );
```

Para probar este código, puedes utilizar el siguiente ejemplo:

```js
const users = [
  { user: "barney", age: 36, active: false },
  { user: "fred", age: 40, active: true }
];
partition(users, (o) => o.active);
// [
//   [{ user: 'fred', age: 40, active: true }],
//   [{ user: 'barney', age: 36, active: false }]
// ]
```

Esto devolverá un arreglo de dos arreglos, donde el primer arreglo contiene todos los elementos para los cuales la función dada devuelve `true`, y el segundo arreglo contiene todos los elementos para los cuales la función dada devuelve `false`.
