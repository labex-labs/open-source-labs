# Diferencia simétrica de arrays

Para encontrar la diferencia simétrica entre dos arrays y incluir valores duplicados, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Crea un `Set` a partir de cada array para obtener los valores únicos de cada uno.
3. Utiliza `Array.prototype.filter()` en cada uno de ellos para conservar solo los valores no contenidos en el otro.

Aquí está el código:

```js
const symmetricDifference = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...a.filter((x) => !sB.has(x)), ...b.filter((x) => !sA.has(x))];
};
```

Puedes utilizar los siguientes ejemplos para probar la función:

```js
symmetricDifference([1, 2, 3], [1, 2, 4]); // [3, 4]
symmetricDifference([1, 2, 2], [1, 3, 1]); // [2, 2, 3]
```
