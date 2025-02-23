# Cómo agrupar y contar elementos en una matriz con JavaScript

Para agrupar y contar elementos en una matriz con JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `Array.prototype.map()` para mapear los valores de una matriz a un nombre de función o propiedad.
3. Utilice el método `Array.prototype.reduce()` para crear un objeto donde las claves se generan a partir de los resultados mapeados.
4. Cree una función llamada `countBy` que tome una matriz y una función como argumentos.
5. Dentro de la función `countBy`, utilice un operador ternario para comprobar si el argumento pasado es una función o un nombre de propiedad. Si es una función, úsela como función de mapeo. Si es un nombre de propiedad, acceda a esa propiedad de los elementos de la matriz.
6. Utilice el método `reduce()` para crear un objeto donde cada clave representa un elemento único en la matriz y su valor es el número de veces que aparece en la matriz.

Aquí está el código:

```js
const countBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => {
      acc[val] = (acc[val] || 0) + 1;
      return acc;
    }, {});
```

Puede probar la función `countBy` con los siguientes ejemplos:

```js
countBy([6.1, 4.2, 6.3], Math.floor); // {4: 1, 6: 2}
countBy(["one", "two", "three"], "length"); // {3: 2, 5: 1}
countBy([{ count: 5 }, { count: 10 }, { count: 5 }], (x) => x.count); // {5: 2, 10: 1}
```
