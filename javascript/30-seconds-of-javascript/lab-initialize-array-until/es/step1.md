# Cómo inicializar una matriz hasta que se cumpla una condición

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

A continuación, se presentan los pasos para inicializar y llenar una matriz con valores generados por una función hasta que se cumpla una determinada condición:

1. Crea una matriz vacía `arr`, una variable de índice `i` y un elemento `el`.
2. Utiliza un bucle `do...while` para agregar elementos a la matriz utilizando la función `mapFn` hasta que la función `conditionFn` devuelva `true` para el índice `i` y el elemento `el` dados.
3. La función `conditionFn` toma tres argumentos: el índice actual, el elemento anterior y la matriz misma.
4. La función `mapFn` toma tres argumentos: el índice actual, el elemento actual y la matriz misma.

Aquí está el código:

```js
const initializeArrayUntil = (conditionFn, mapFn) => {
  const arr = [];
  let i = 0;
  let el = undefined;
  do {
    el = mapFn(i, el, arr);
    arr.push(el);
    i++;
  } while (!conditionFn(i, el, arr));
  return arr;
};
```

Para utilizar la función `initializeArrayUntil`, proporciona dos funciones como argumentos:

```js
initializeArrayUntil(
  (i, val) => val > 10, //conditionFn
  (i, val, arr) => (i <= 1 ? 1 : val + arr[i - 2]) //mapFn
); // [1, 1, 2, 3, 5, 8, 13]
```

Este código inicializa una matriz con la secuencia de Fibonacci hasta el primer número mayor que 10. La función `conditionFn` comprueba si el valor actual es mayor que 10, y la función `mapFn` genera el siguiente número de la secuencia.
