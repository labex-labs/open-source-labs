# Comprobación de la igualdad de los elementos de un array

Para comprobar si todos los elementos de un array son iguales, puedes utilizar el método `Array.prototype.every()`, que compara todos los elementos con el primero.

Aquí está cómo puedes implementarlo:

```js
const allEqual = (arr) => arr.every((val) => val === arr[0]);
```

Tenga en cuenta que se utiliza el operador de `comparación estricta` para comparar los elementos. Este operador no tiene en cuenta la auto-desigualdad de `NaN`.

Uso de ejemplo:

```js
allEqual([1, 2, 3, 4, 5, 6]); // false
allEqual([1, 1, 1, 1]); // true
```
