# Función de Diferencia Simétrica Única de Arrays

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. La siguiente función devuelve la diferencia simétrica única entre dos arrays. Elimina los valores duplicados de cualquiera de los arrays.

Para lograr esto, utiliza `Array.prototype.filter()` y `Array.prototype.includes()` en cada array para eliminar los valores contenidos en el otro. Crea un `Set` a partir de los resultados para eliminar los valores duplicados.

```js
const uniqueSymmetricDifference = (a, b) => [
  ...new Set([
    ...a.filter((v) => !b.includes(v)),
    ...b.filter((v) => !a.includes(v))
  ])
];
```

Utiliza la función como se muestra a continuación:

```js
uniqueSymmetricDifference([1, 2, 3], [1, 2, 4]); // [3, 4]
uniqueSymmetricDifference([1, 2, 2], [1, 3, 1]); // [2, 3]
```
