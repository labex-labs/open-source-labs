# Filtrar valores únicos de una matriz basados en una función

Aquí está cómo crear una matriz que contiene solo los valores no únicos al filtrar los valores únicos basados en una función comparadora, `fn`:

```js
const filterUniqueBy = (arr, fn) =>
  arr.filter((v, i) => arr.some((x, j) => (i !== j) === fn(v, x, i, j)));
```

Para usar esta función, llame a `filterUniqueBy()` con dos argumentos: la matriz que desea filtrar y la función comparadora. La función comparadora debe tomar cuatro argumentos: los valores de los dos elementos que se están comparando y sus índices.

Por ejemplo, si tiene una matriz de objetos y desea filtrar los objetos con valores únicos de `id`, puede hacer lo siguiente:

```js
filterUniqueBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 3, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'a' }, { id: 0, value: 'e' } ]
```

Para comenzar a practicar la codificación, abra la Terminal/SSH y escriba `node`.
