# Cómo negar una función predicado en JavaScript

Para negar una función predicado en JavaScript, puedes usar el operador `!`. Para hacer esto, puedes crear una función de orden superior llamada `negate` que tome una función predicado y le aplique el operador `!` con sus argumentos. Aquí hay un ejemplo de cómo implementar `negate`:

```js
const negate =
  (func) =>
  (...args) =>
    !func(...args);
```

Luego puedes usar `negate` para negar cualquier función predicado. Aquí hay un ejemplo de cómo usar `negate` para filtrar los números pares de un array:

```js
const isEven = (n) => n % 2 === 0;
const isOdd = negate(isEven);

[1, 2, 3, 4, 5, 6].filter(isOdd); // [ 1, 3, 5 ]
```

En este ejemplo, `isEven` es una función predicado que verifica si un número es par. Luego usamos `negate` para crear una nueva función predicado llamada `isOdd` que verifica si un número es impar negando `isEven`. Finalmente, usamos `isOdd` con el método `filter` para filtrar los números pares del array.
