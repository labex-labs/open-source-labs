# Cómo alternar un elemento en una matriz

Para alternar un elemento en una matriz, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Verifica si el elemento dado está en la matriz utilizando `Array.prototype.includes()`.
3. Si el elemento está en la matriz, utiliza `Array.prototype.filter()` para eliminarlo.
4. Si el elemento no está en la matriz, utiliza el operador de propagación (`...`) para agregarlo.
5. Utiliza la función `toggleElement`, que acepta una matriz y un valor, para alternar el elemento en la matriz.

```js
const toggleElement = (arr, val) =>
  arr.includes(val) ? arr.filter((el) => el !== val) : [...arr, val];

toggleElement([1, 2, 3], 2); // [1, 3]
toggleElement([1, 2, 3], 4); // [1, 2, 3, 4]
```

Siguiendo estos pasos, puedes alternar fácilmente un elemento en una matriz utilizando JavaScript.
