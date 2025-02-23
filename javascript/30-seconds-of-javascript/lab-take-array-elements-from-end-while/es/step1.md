# Eliminando elementos de un array desde el final hasta que se cumpla una condición

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Aquí hay una función que elimina elementos del final de un array hasta que la función pasada devuelva `false`. Luego devuelve los elementos eliminados.

Para utilizarla, crea una copia invertida del array utilizando el operador de propagación (`...`) y `Array.prototype.reverse()`. Luego, recorre la copia invertida utilizando un bucle `for...of` sobre `Array.prototype.entries()` hasta que el valor devuelto por la función sea falso.

La función de devolución de llamada, `fn`, acepta un solo argumento que es el valor del elemento. Finalmente, devuelve los elementos eliminados utilizando `Array.prototype.slice()`.

```js
const takeRightWhile = (arr, fn) => {
  for (const [i, val] of [...arr].reverse().entries())
    if (!fn(val)) return i === 0 ? [] : arr.slice(-i);
  return arr;
};
```

Aquí hay un ejemplo de cómo utilizar la función:

```js
takeRightWhile([1, 2, 3, 4], (n) => n >= 3); // [3, 4]
```
