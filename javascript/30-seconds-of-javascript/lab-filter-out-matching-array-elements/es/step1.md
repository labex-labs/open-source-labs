# Cómo filtrar elementos de un array que coinciden en JavaScript

Para filtrar elementos de un array de JavaScript que tienen uno o más valores especificados, siga estos pasos:

1. Abra la Terminal o SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `Array.prototype.includes()` para encontrar los valores a excluir.
3. Utilice el método `Array.prototype.filter()` para crear un nuevo array con los elementos excluidos.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const without = (arr, ...args) => arr.filter((v) => !args.includes(v));

without([2, 1, 2, 3], 1, 2); // [3]
```

En este ejemplo, la función `without` toma un array `arr` y uno o más argumentos `args`. La función utiliza el método `filter()` para crear un nuevo array que excluye cualquier elemento que coincida con cualquiera de los valores especificados en `args`. El método `includes()` se utiliza para comprobar si el valor está en `args`. Finalmente, la función devuelve el nuevo array con los elementos excluidos.
