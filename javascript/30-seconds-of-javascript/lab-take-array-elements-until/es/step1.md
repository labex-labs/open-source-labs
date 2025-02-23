# Eliminación de elementos de un arreglo hasta que se cumpla una condición

Para eliminar elementos de un arreglo hasta que se cumpla una condición y obtener los elementos eliminados, siga los pasos siguientes:

- Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
- Recorra el arreglo utilizando un bucle `for...of` sobre `Array.prototype.entries()` hasta que la función pasada como argumento devuelva un valor verdadero.
- Utilice `Array.prototype.slice()` para devolver los elementos eliminados.
- La función de devolución de llamada, `fn`, acepta un solo argumento que es el valor del elemento.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const takeUntil = (arr, fn) => {
  for (const [i, val] of arr.entries()) if (fn(val)) return arr.slice(0, i);
  return arr;
};

takeUntil([1, 2, 3, 4], (n) => n >= 3); // [1, 2]
```

En el ejemplo anterior, la función `takeUntil()` se utiliza para eliminar elementos del arreglo `[1, 2, 3, 4]` hasta que el valor sea mayor o igual a 3. La salida es `[1, 2]`.
