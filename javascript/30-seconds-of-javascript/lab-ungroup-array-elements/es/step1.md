# Cómo desagrupar elementos de un array en JavaScript

Para desagrupar los elementos de un array producido por la función `zip`, puedes crear una matriz de matrices utilizando la función `unzip` en JavaScript. Aquí está cómo:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `Math.max()`, `Function.prototype.apply()` para obtener la submatriz más larga en el array, y `Array.prototype.map()` para convertir cada elemento en un array.
3. Utiliza `Array.prototype.reduce()` y `Array.prototype.forEach()` para mapear los valores agrupados a arrays individuales.

Aquí está el código para la función `unzip`:

```js
const unzip = (arr) =>
  arr.reduce(
    (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
    Array.from({
      length: Math.max(...arr.map((x) => x.length))
    }).map((x) => [])
  );
```

Puedes utilizar la función `unzip` con los siguientes ejemplos:

```js
unzip([
  ["a", 1, true],
  ["b", 2, false]
]); // [['a', 'b'], [1, 2], [true, false]]
unzip([
  ["a", 1, true],
  ["b", 2]
]); // [['a', 'b'], [1, 2], [true]]
```

Siguiendo estos pasos, puedes desagrupar fácilmente los elementos de un array en JavaScript.
