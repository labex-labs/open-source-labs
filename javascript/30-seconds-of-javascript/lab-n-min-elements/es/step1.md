# Función para Devolver los N Elementos Mínimos de una Matriz

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. Utiliza la función `minN` para devolver los `n` elementos mínimos de una matriz.

Aquí está cómo utilizar la función:

- Utiliza `Array.prototype.sort()` y el operador de propagación (`...`) para crear una copia superficial de la matriz y ordenarla en orden ascendente.
- Utiliza `Array.prototype.slice()` para obtener el número especificado de elementos.
- Si omites el segundo argumento, `n`, la función devolverá una matriz de un solo elemento.
- Si `n` es mayor o igual que la longitud de la matriz proporcionada, la función devolverá la matriz original, ordenada en orden ascendente.

```js
const minN = (arr, n = 1) => [...arr].sort((a, b) => a - b).slice(0, n);
```

Aquí hay algunos ejemplos:

```js
minN([1, 2, 3]); // [1]
minN([1, 2, 3], 2); // [1, 2]
```
