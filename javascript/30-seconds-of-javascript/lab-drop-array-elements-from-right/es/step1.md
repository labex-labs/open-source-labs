# Eliminar elementos de un array desde la derecha

Para eliminar un número especificado de elementos desde la derecha de un array, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.slice()` para eliminar el número especificado de elementos desde la derecha.
3. Si desea eliminar solo un elemento, puede omitir el último argumento, `n`, y se utilizará el valor predeterminado de `1`.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const dropRight = (arr, n = 1) => arr.slice(0, -n);
```

Puede probar esta función con los siguientes ejemplos:

```js
dropRight([1, 2, 3]); // [1, 2]
dropRight([1, 2, 3], 2); // [1]
dropRight([1, 2, 3], 42); // []
```
