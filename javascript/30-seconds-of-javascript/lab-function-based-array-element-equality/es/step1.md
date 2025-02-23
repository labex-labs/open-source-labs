# Comprobando si los elementos de un array son iguales con una función dada

Para comprobar si todos los elementos de un array son iguales, utiliza la función `allEqualBy`. Esta función aplica una función de asignación `fn` dada al primer elemento del array `arr`. Luego, comprueba si `fn` devuelve el mismo valor para todos los elementos del array que para el primer elemento, utilizando `Array.prototype.every()`. La función utiliza el operador de comparación estricta, que no tiene en cuenta la auto-desigualdad de `NaN`.

Aquí está el código de `allEqualBy`:

```js
const allEqualBy = (arr, fn) => {
  const eql = fn(arr[0]);
  return arr.every((val) => fn(val) === eql);
};
```

Puedes utilizar `allEqualBy` de la siguiente manera:

```js
allEqualBy([1.1, 1.2, 1.3], Math.round); // true
allEqualBy([1.1, 1.3, 1.6], Math.round); // false
```

Para comenzar a practicar la codificación con esta función, abre la Terminal/SSH y escribe `node`.
