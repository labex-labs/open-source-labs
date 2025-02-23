# Cómo agrupar elementos de un array

Si quieres practicar la codificación, puedes comenzar abriendo la Terminal/SSH y escribiendo `node`. Una vez que estés listo, puedes agrupar los elementos de un array basados en una función dada siguiendo los siguientes pasos:

1. Utiliza `Array.prototype.map()` para mapear los valores del array a un nombre de función o propiedad.
2. Utiliza `Array.prototype.reduce()` para crear un objeto donde las claves se generan a partir de los resultados mapeados.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const groupBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val, i) => {
      acc[val] = (acc[val] || []).concat(arr[i]);
      return acc;
    }, {});
```

Para probar el código, puedes utilizar los siguientes ejemplos:

```js
groupBy([6.1, 4.2, 6.3], Math.floor); // {4: [4.2], 6: [6.1, 6.3]}
groupBy(["one", "two", "three"], "length"); // {3: ['one', 'two'], 5: ['three']}
```

Estos devolverán objetos con claves basadas en la función especificada y valores que son arrays de los elementos originales que coinciden con la función.
