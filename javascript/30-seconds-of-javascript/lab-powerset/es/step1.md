# Cómo generar el conjunto potencia en JavaScript

Para generar el conjunto potencia de una matriz dada de números en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `Array.prototype.reduce()` combinado con el método `Array.prototype.map()` para iterar sobre los elementos y combinarlos en una matriz que contenga todas las combinaciones.
3. Implemente el siguiente código:

```js
const powerset = (arr) =>
  arr.reduce((a, v) => a.concat(a.map((r) => r.concat(v))), [[]]);
```

4. Para generar el conjunto potencia, llame a la función `powerset()` y pase la matriz como argumento. Por ejemplo:

```js
powerset([1, 2]); // [[], [1], [2], [1, 2]]
```

Esto devolverá una matriz que contiene todos los subconjuntos posibles de la matriz dada.
