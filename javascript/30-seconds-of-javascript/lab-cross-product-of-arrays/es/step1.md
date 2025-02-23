# Crear un producto cruzado de matrices en JavaScript

Para crear un producto cruzado de matrices en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.reduce()`, `Array.prototype.map()` y `Array.prototype.concat()` para producir cada posible pareja a partir de los elementos de las dos matrices.
3. La función `xProd()` toma dos matrices como argumentos y crea una nueva matriz a partir de las dos suministradas creando cada posible pareja a partir de las matrices.
4. Aquí hay un ejemplo de la función `xProd()` en acción:

```js
const xProd = (a, b) =>
  a.reduce((acc, x) => acc.concat(b.map((y) => [x, y])), []);

xProd([1, 2], ["a", "b"]); // [[1, 'a'], [1, 'b'], [2, 'a'], [2, 'b']]
```

Esto devolverá una matriz que contiene todas las posibles parejas de elementos de las dos matrices de entrada.
