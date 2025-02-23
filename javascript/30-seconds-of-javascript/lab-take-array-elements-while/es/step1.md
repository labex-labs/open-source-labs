# Eliminación de elementos de un array basados en una condición

Para eliminar elementos de un array basados en una condición, abra la Terminal/SSH y escriba `node`.

La función `takeWhile` elimina elementos de un array hasta que la función pasada devuelve `false`, y luego devuelve los elementos eliminados.

A continuación se presentan los pasos para utilizar la función `takeWhile`:

- Recorra el array utilizando un bucle `for...of` sobre `Array.prototype.entries()`.
- Siga el bucle hasta que el valor devuelto por la función sea falso.
- Devuelva los elementos eliminados utilizando `Array.prototype.slice()`.
- La función de devolución de llamada `fn` acepta un solo argumento que es el valor del elemento.

Utilice el siguiente código para implementar la función `takeWhile`:

```js
const takeWhile = (arr, fn) => {
  for (const [i, val] of arr.entries()) if (!fn(val)) return arr.slice(0, i);
  return arr;
};
```

A continuación se muestra un ejemplo de uso de la función `takeWhile` para eliminar elementos de un array basados en una condición:

```js
takeWhile([1, 2, 3, 4], (n) => n < 3); // [1, 2]
```
