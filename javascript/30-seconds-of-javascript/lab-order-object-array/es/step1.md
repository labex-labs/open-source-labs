# Cómo ordenar una matriz de objetos en JavaScript

Para ordenar una matriz de objetos en JavaScript, puedes utilizar el método `Array.prototype.sort()` y el método `Array.prototype.reduce()` en la matriz `props` con un valor predeterminado de `0`.

A continuación, hay una función de ejemplo, `orderBy`, que ordena una matriz de objetos según las propiedades y órdenes especificadas:

```js
const orderBy = (arr, props, orders = ["asc"]) =>
  [...arr].sort((a, b) =>
    props.reduce((acc, prop, i) => {
      if (acc === 0) {
        const [p1, p2] =
          orders[i] === "desc" ? [b[prop], a[prop]] : [a[prop], b[prop]];
        acc = p1 > p2 ? 1 : p1 < p2 ? -1 : 0;
      }
      return acc;
    }, 0)
  );
```

Para utilizar esta función, pasa una matriz de objetos, una matriz de propiedades por las que ordenar y una matriz opcional de órdenes. Si no se proporciona una matriz `orders`, la función ordenará por `'asc'` por defecto.

A continuación, hay algunos ejemplos de cómo utilizar la función `orderBy`:

```js
const users = [
  { name: "fred", age: 48 },
  { name: "barney", age: 36 },
  { name: "fred", age: 40 }
];

// ordenar por nombre ascendente y edad descendente
orderBy(users, ["name", "age"], ["asc", "desc"]);
// Salida: [{name: 'barney', age: 36}, {name: 'fred', age: 48}, {name: 'fred', age: 40}]

// ordenar por nombre ascendente y edad ascendente (orden predeterminado)
orderBy(users, ["name", "age"]);
// Salida: [{name: 'barney', age: 36}, {name: 'fred', age: 40}, {name: 'fred', age: 48}]
```
