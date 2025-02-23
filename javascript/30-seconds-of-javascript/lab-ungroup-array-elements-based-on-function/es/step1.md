# Cómo desagrupar elementos de un array en función de una función

Si necesitas desagrupar los elementos de un array producido por `zip` y aplicar una función, puedes utilizar `unzipWith`. Aquí te muestro cómo implementarlo:

1. Utiliza `Math.max()` y el operador de propagación (`...`) para obtener la submatriz más larga del array y `Array.prototype.map()` para convertir cada elemento en un array.
2. Utiliza `Array.prototype.reduce()` y `Array.prototype.forEach()` para mapear los valores agrupados a arrays individuales.
3. Utiliza `Array.prototype.map()` y el operador de propagación (`...`) para aplicar `fn` a cada grupo individual de elementos.

```js
const unzipWith = (arr, fn) =>
  arr
    .reduce(
      (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
      Array.from({
        length: Math.max(...arr.map((x) => x.length))
      }).map((x) => [])
    )
    .map((val) => fn(...val));
```

Para utilizar `unzipWith`, abre la Terminal/SSH y escribe `node`. Luego, puedes ejecutar el siguiente ejemplo:

```js
unzipWith(
  [
    [1, 10, 100],
    [2, 20, 200]
  ],
  (...args) => args.reduce((acc, v) => acc + v, 0)
);
// [3, 30, 300]
```

Esto creará un array de elementos desagrupando los elementos del array de entrada producido por `zip` y aplicando la función proporcionada.
