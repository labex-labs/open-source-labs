# Eliminando elementos coincidentes de una matriz

Para eliminar elementos específicos de una matriz basados en una condición dada, puedes utilizar la función `remove`. Esta función modifica la matriz original eliminando los elementos para los cuales la función dada devuelve `false`.

A continuación se presentan los pasos para utilizar la función `remove`:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.filter()` para encontrar los elementos de la matriz que devuelven valores verdaderos.
3. Utilice `Array.prototype.reduce()` para eliminar los elementos utilizando `Array.prototype.splice()`.
4. La función de devolución de llamada se invoca con tres argumentos (valor, índice, matriz).

```js
const remove = (arr, func) =>
  Array.isArray(arr)
    ? arr.filter(func).reduce((acc, val) => {
        arr.splice(arr.indexOf(val), 1);
        return acc.concat(val);
      }, [])
    : [];
```

A continuación se muestra un ejemplo de uso de la función `remove`:

```js
remove([1, 2, 3, 4], (n) => n % 2 === 0); // [2, 4]
```

Esto devolverá una nueva matriz con los elementos eliminados.
