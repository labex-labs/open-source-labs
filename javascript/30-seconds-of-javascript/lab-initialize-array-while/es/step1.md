# Cómo inicializar y llenar una matriz con un bucle while en JavaScript

Para comenzar a practicar la programación en JavaScript, abre la Terminal/SSH y escribe `node`.

La función `initializeArrayWhile` inicializa y llena una matriz con valores generados por una función mientras se cumpla una condición. Aquí cómo funciona:

1. Crea una matriz vacía llamada `arr`, una variable de índice llamada `i` y un elemento llamado `el`.
2. Utiliza un bucle `while` para agregar elementos a la matriz utilizando la función `mapFn`, siempre y cuando la función `conditionFn` devuelva `true` para el índice `i` y el elemento `el` dados.
3. La función `conditionFn` toma tres argumentos: el índice actual, el elemento anterior y la matriz misma.
4. La función `mapFn` toma tres argumentos: el índice actual, el elemento actual y la matriz misma.
5. La función `initializeArrayWhile` devuelve la matriz.

Aquí está el código:

```js
const initializeArrayWhile = (conditionFn, mapFn) => {
  const arr = [];
  let i = 0;
  let el = mapFn(i, undefined, arr);
  while (conditionFn(i, el, arr)) {
    arr.push(el);
    i++;
    el = mapFn(i, el, arr);
  }
  return arr;
};
```

Puedes utilizar la función `initializeArrayWhile` para inicializar y llenar una matriz con valores. Por ejemplo:

```js
initializeArrayWhile(
  (i, val) => val < 10,
  (i, val, arr) => (i <= 1 ? 1 : val + arr[i - 2])
); // [1, 1, 2, 3, 5, 8]
```
