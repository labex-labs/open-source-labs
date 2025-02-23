# Encontrando valores únicos en una matriz con una función

Para encontrar todos los valores únicos de una matriz, proporciona una función comparadora.

Utiliza `Array.prototype.reduce()` y `Array.prototype.some()` para crear una matriz que contenga solo la primera aparición única de cada valor. La función comparadora `fn` toma dos argumentos, los valores de los dos elementos que se están comparando.

```js
const uniqueElementsBy = (arr, fn) =>
  arr.reduce((acc, v) => {
    if (!acc.some((x) => fn(v, x))) acc.push(v);
    return acc;
  }, []);
```

Para probar la función, utiliza el ejemplo siguiente:

```js
uniqueElementsBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'a' }, { id: 1, value: 'b' }, { id: 2, value: 'c' } ]
```

Comienza a practicar la codificación abriendo la Terminal/SSH y escribiendo `node`.
