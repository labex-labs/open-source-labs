# Función para Obtener el Tamaño de una Matriz, Objeto o Cadena

Para utilizar esta función, abra la Terminal/SSH y escriba `node`. Esta función obtiene el tamaño de una matriz, objeto o cadena.

Para utilizarlas:

- Determine el tipo de `val` (`array`, `object` o `string`).
- Utilice la propiedad `Array.prototype.length` para matrices.
- Utilice el valor `length` o `size` si está disponible, o la cantidad de claves para objetos.
- Para cadenas, utilice el `size` de un objeto [`Blob`](https://developer.mozilla.org/es/docs/Web/API/Blob) creado a partir de `val`.

```js
const size = (val) =>
  Array.isArray(val)
    ? val.length
    : val && typeof val === "object"
      ? val.size || val.length || Object.keys(val).length
      : typeof val === "string"
        ? new Blob([val]).size
        : 0;
```

Ejemplos:

```js
size([1, 2, 3, 4, 5]); // 5
size("size"); // 4
size({ one: 1, two: 2, three: 3 }); // 3
```
