# Función de JavaScript para Encontrar el Último Valor Coincidente

Para encontrar el último elemento en una matriz que cumpla una condición dada, utiliza la siguiente función de JavaScript:

```js
const findLast = (arr, fn) => arr.filter(fn).pop();
```

Para utilizar esta función, pasa la matriz en la que quieres buscar y una función que devuelva un valor verdadero para los elementos que quieres coincidir.

Por ejemplo, `findLast([1, 2, 3, 4], n => n % 2 === 1);` devolverá `3`, ya que encuentra el último número impar en la matriz.

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.
