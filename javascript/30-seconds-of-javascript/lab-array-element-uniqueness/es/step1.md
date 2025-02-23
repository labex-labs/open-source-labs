# Cómo comprobar si todos los elementos de una matriz son únicos

Para comprobar si todos los elementos de una matriz son únicos, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Cree un nuevo `Set` a partir de los valores mapeados para conservar solo las ocurrencias únicas.
3. Utilice `Array.prototype.length` y `Set.prototype.size` para comparar la longitud de los valores únicos con la matriz original.

A continuación, se muestra una función de ejemplo que implementa estos pasos:

```js
const allUnique = (arr) => arr.length === new Set(arr).size;
```

Puede utilizar esta función para comprobar si una matriz tiene todos los elementos únicos de la siguiente manera:

```js
allUnique([1, 2, 3, 4]); // true
allUnique([1, 1, 2, 3]); // false
```
