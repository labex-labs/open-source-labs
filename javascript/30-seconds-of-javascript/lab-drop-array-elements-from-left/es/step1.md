# Eliminando elementos de un array desde la izquierda

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Aquí hay una función que crea una nueva matriz con un número especificado de elementos eliminados desde la izquierda:

```js
const drop = (arr, n = 1) => arr.slice(n);
```

La función utiliza `Array.prototype.slice()` para eliminar el número especificado de elementos desde la izquierda. Si omites el último argumento, `n`, la función utilizará un valor predeterminado de `1`.

Aquí hay algunos ejemplos de uso de la función `drop`:

```js
drop([1, 2, 3]); // [2, 3]
drop([1, 2, 3], 2); // [3]
drop([1, 2, 3], 42); // []
```
