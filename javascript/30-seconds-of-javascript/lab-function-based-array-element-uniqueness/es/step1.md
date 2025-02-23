# Comprobando si todos los elementos de una matriz son únicos con una función

Para comprobar si todos los elementos de una matriz son únicos en función de una función de asignación proporcionada, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `Array.prototype.map()` para aplicar la función `fn` proporcionada a todos los elementos de la matriz `arr`.
3. Cree un nuevo `Set` a partir de los valores mapeados para conservar solo las ocurrencias únicas.
4. Compare la longitud de los valores mapeados únicos con la longitud de la matriz original utilizando los métodos `Array.prototype.length` y `Set.prototype.size`.

Aquí está el código:

```js
const allUniqueBy = (arr, fn) => arr.length === new Set(arr.map(fn)).size;
```

Puede utilizar la función `allUniqueBy()` para comprobar si todos los elementos de una matriz son únicos. Por ejemplo:

```js
allUniqueBy([1.2, 2.4, 2.9], Math.round); // true
allUniqueBy([1.2, 2.3, 2.4], Math.round); // false
```
