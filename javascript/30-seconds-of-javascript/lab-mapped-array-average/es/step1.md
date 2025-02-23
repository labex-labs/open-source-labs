# Instrucciones para calcular el promedio de un array mapeado

Para calcular el promedio de un array, puedes mapear cada elemento a un nuevo valor utilizando la función proporcionada. Aquí están los pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `Array.prototype.map()` para mapear cada elemento al valor devuelto por `fn`.
3. Utiliza `Array.prototype.reduce()` para sumar cada valor mapeado a un acumulador, inicializado con un valor de `0`.
4. Divide el array resultante entre su longitud para obtener el promedio.

Aquí está el código que puedes utilizar:

```js
const averageBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => acc + val, 0) / arr.length;
```

Puedes probar esta función utilizando los siguientes ejemplos:

```js
averageBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (o) => o.n); // 5
averageBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 5
```
