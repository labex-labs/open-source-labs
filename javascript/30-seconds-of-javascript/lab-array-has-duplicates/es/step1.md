# Cómo comprobar duplicados en un array

Para comprobar si un array tiene valores duplicados, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Set` para obtener los valores únicos del array.
3. Utilice `Set.prototype.size` y `Array.prototype.length` para comprobar si la cantidad de valores únicos es la misma que el número de elementos en el array original.

A continuación, se muestra un fragmento de código de ejemplo que comprueba duplicados en un array:

```js
const hasDuplicates = (arr) => new Set(arr).size !== arr.length;
```

Puede probar esta función con el siguiente código:

```js
hasDuplicates([0, 1, 1, 2]); // true
hasDuplicates([0, 1, 2, 3]); // false
```

La función `hasDuplicates` devuelve `true` si hay valores duplicados en el array, y `false` en caso contrario.
