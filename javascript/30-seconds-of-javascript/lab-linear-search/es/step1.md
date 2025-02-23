# Algoritmo de búsqueda lineal

Para practicar la codificación, abre la Terminal o SSH y escribe `node`. El algoritmo de búsqueda lineal encuentra el primer índice de un elemento dado en un array.

Así es como funciona:

- Utiliza un bucle `for...in` para iterar sobre los índices del array dado.
- Verifica si el elemento en el índice correspondiente es igual a `item`.
- Si se encuentra el elemento, devuelve el índice. Utiliza el operador unario `+` para convertirlo de una cadena a un número.
- Si el elemento no se encuentra después de iterar sobre todo el array, devuelve `-1`.

Aquí está el código:

```js
const linearSearch = (arr, item) => {
  for (const i in arr) {
    if (arr[i] === item) return +i;
  }
  return -1;
};
```

Para probar la función, llámala con un array y un valor a buscar:

```js
linearSearch([2, 9, 9], 9); // 1
linearSearch([2, 9, 9], 7); // -1
```
