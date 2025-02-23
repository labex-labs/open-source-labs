# Producto Cartesiano

Para calcular el producto cartesiano de dos arrays, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.reduce()`, `Array.prototype.map()` y el operador de propagación (`...`) para generar todos los posibles pares de elementos a partir de los dos arrays.
3. Utilice el siguiente código:

```js
const cartesianProduct = (a, b) =>
  a.reduce((p, x) => [...p, ...b.map((y) => [x, y])], []);
```

Ejemplo:

```js
cartesianProduct(["x", "y"], [1, 2]);
// [['x', 1], ['x', 2], ['y', 1], ['y', 2]]
```

Esto generará todas las posibles combinaciones de elementos de los dos arrays.
