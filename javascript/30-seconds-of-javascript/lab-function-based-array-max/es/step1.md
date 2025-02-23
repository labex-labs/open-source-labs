# Cómo encontrar el valor máximo de una matriz basado en una función

Para encontrar el valor máximo de una matriz basado en una función, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.map()` para mapear cada elemento de la matriz al valor devuelto por la función proporcionada, `fn`.
3. Utilice `Math.max()` para obtener el valor máximo de la matriz mapeada.

A continuación, se muestra un fragmento de código de ejemplo que implementa los pasos anteriores:

```js
const maxBy = (arr, fn) =>
  Math.max(...arr.map(typeof fn === "function" ? fn : (val) => val[fn]));
```

Para utilizar la función `maxBy`, pase una matriz y la función que se debe utilizar para mapear cada elemento a un valor. Puede pasar una función directamente o una cadena que represente la clave que se debe utilizar para acceder al valor en cada objeto de la matriz.

A continuación, se muestran algunos llamados de ejemplo a la función `maxBy`:

```js
maxBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // devuelve 8
maxBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // devuelve 8
```
