# Diferencia simétrica de arrays mapeados

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`.

Esta función devuelve la diferencia simétrica entre dos arrays, después de aplicar la función proporcionada a cada elemento de ambos arrays. Aquí cómo funciona:

- Crea un `Set` a partir de cada array para obtener los valores únicos de cada uno después de aplicar `fn` a ellos.
- Utiliza `Array.prototype.filter()` en cada uno de ellos para conservar solo los valores no contenidos en el otro.

Aquí está el código de la función `symmetricDifferenceBy`:

```js
const symmetricDifferenceBy = (a, b, fn) => {
  const sA = new Set(a.map((v) => fn(v))),
    sB = new Set(b.map((v) => fn(v)));
  return [
    ...a.filter((x) => !sB.has(fn(x))),
    ...b.filter((x) => !sA.has(fn(x)))
  ];
};
```

Puedes utilizar `symmetricDifferenceBy` de la siguiente manera:

```js
symmetricDifferenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [ 1.2, 3.4 ]
symmetricDifferenceBy(
  [{ id: 1 }, { id: 2 }, { id: 3 }],
  [{ id: 1 }, { id: 2 }, { id: 4 }],
  (i) => i.id
);
// [{ id: 3 }, { id: 4 }]
```
