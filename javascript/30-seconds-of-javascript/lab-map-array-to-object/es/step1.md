# Mapear un arreglo a un objeto

Para mapear los valores de un arreglo a un objeto utilizando una función, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar la práctica de codificación.
2. Utiliza `Array.prototype.reduce()` para aplicar `fn` a cada elemento en `arr` y combinar los resultados en un objeto.
3. Utiliza `el` como la clave para cada propiedad y el resultado de `fn` como el valor.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const mapObject = (arr, fn) =>
  arr.reduce((acc, el, i) => {
    acc[el] = fn(el, i, arr);
    return acc;
  }, {});
```

Puedes utilizar la función `mapObject` como se muestra en este ejemplo:

```js
mapObject([1, 2, 3], (a) => a * a); // { 1: 1, 2: 4, 3: 9 }
```
