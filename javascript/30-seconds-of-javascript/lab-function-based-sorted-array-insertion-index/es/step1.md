# Función para encontrar el índice de inserción en un array ordenado

Para encontrar el índice más bajo para insertar un valor en un array y mantener su orden de clasificación, utiliza la función `sortedIndexBy(arr, n, fn)` en JavaScript.

Esta función comprueba de manera aproximada si el array está ordenado en orden descendente y luego utiliza `Array.prototype.findIndex()` para encontrar el índice adecuado basado en la función iteradora `fn`.

Aquí está el código de la función `sortedIndexBy()`:

```js
const sortedIndexBy = (arr, n, fn) => {
  const isDescending = fn(arr[0]) > fn(arr[arr.length - 1]);
  const val = fn(n);
  const index = arr.findIndex((el) =>
    isDescending ? val >= fn(el) : val <= fn(el)
  );
  return index === -1 ? arr.length : index;
};
```

Puedes llamar a la función con un array de objetos, un valor para insertar y una función iteradora.

Por ejemplo, `sortedIndexBy([{ x: 4 }, { x: 5 }], { x: 4 }, o => o.x)` devuelve `0`, que es el índice donde se debe insertar el objeto `{ x: 4 }` para mantener el orden de clasificación basado en la propiedad `x`.
