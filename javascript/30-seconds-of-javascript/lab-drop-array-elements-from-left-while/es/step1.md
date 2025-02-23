# Eliminación de elementos de un array basada en una función

Para eliminar elementos específicos de un array, utiliza la función `dropWhile`, que elimina elementos hasta que la función pasada devuelva `true`. La función luego devuelve los elementos restantes del array.

Así es como funciona:

- Recorre el array utilizando `Array.prototype.slice()` para eliminar el primer elemento del array hasta que el valor devuelto por `func` sea `true`.
- Devuelve los elementos restantes.

Uso de ejemplo:

```js
const dropWhile = (arr, func) => {
  while (arr.length > 0 && !func(arr[0])) arr = arr.slice(1);
  return arr;
};

dropWhile([1, 2, 3, 4], (n) => n >= 3); // [3, 4]
```

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.
