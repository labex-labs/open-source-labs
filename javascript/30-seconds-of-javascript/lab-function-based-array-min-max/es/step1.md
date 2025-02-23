# Cómo encontrar el mínimo y el máximo de una matriz utilizando una función proporcionada

Para practicar la codificación, abre la Terminal o SSH y escribe `node`.

Aquí hay una función que devuelve los valores mínimo y máximo de una matriz, basada en una función proporcionada que establece la regla de comparación:

```js
const reduceWhich = (arr, comparator = (a, b) => a - b) =>
  arr.reduce((a, b) => (comparator(a, b) >= 0 ? b : a));
```

Para utilizarla, sigue estos pasos:

1. Llama a `reduceWhich` con la matriz que quieres procesar y la función `comparator` opcional.
2. La función `reduceWhich` utilizará `Array.prototype.reduce()` en combinación con la función `comparator` para devolver el elemento adecuado de la matriz.
3. Si omites el segundo argumento (`comparator`), se utilizará la función predeterminada, que devuelve el elemento mínimo de la matriz.

Aquí hay algunos ejemplos de cómo utilizar `reduceWhich`:

```js
reduceWhich([1, 3, 2]); // 1
reduceWhich([1, 3, 2], (a, b) => b - a); // 3
reduceWhich(
  [
    { name: "Tom", age: 12 },
    { name: "Jack", age: 18 },
    { name: "Lucy", age: 9 }
  ],
  (a, b) => a.age - b.age
); // {name: 'Lucy', age: 9}
```

En los ejemplos anteriores, la primera llamada a `reduceWhich` devuelve el valor mínimo de la matriz `[1, 3, 2]`, que es `1`. La segunda llamada devuelve el valor máximo de la misma matriz, basada en la función `comparator` que invierte el orden de comparación. La tercera llamada devuelve el objeto en la matriz que tiene la propiedad `age` mínima, basada en la función `comparator` que compara las propiedades `age` de los objetos.
