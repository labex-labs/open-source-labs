# Eliminando elementos de un array desde el final hasta que se cumpla una condición

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Esta función elimina elementos del final de un array hasta que la función pasada devuelva `true`, y luego devuelve los elementos eliminados.

A continuación se muestra cómo funciona:

- Primero, crea una copia invertida del array utilizando el operador de propagación (`...`) y `Array.prototype.reverse()`.
- A continuación, recorre la copia invertida utilizando un bucle `for...of` sobre `Array.prototype.entries()` hasta que el valor devuelto por la función sea verdadero.
- Después de eso, devuelve los elementos eliminados utilizando `Array.prototype.slice()`.
- La función de devolución de llamada, `fn`, acepta un solo argumento que es el valor del elemento.

Aquí está el código:

```js
const takeRightUntil = (arr, fn) => {
  for (const [i, val] of [...arr].reverse().entries())
    if (fn(val)) return i === 0 ? [] : arr.slice(-i);
  return arr;
};
```

A continuación se muestra un ejemplo de cómo utilizar esta función:

```js
takeRightUntil([1, 2, 3, 4], (n) => n < 3); // [3, 4]
```
