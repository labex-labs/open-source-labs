# Cómo calcular el promedio de números en JavaScript

Para calcular el promedio de dos o más números en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método integrado `Array.prototype.reduce()` para sumar cada valor a un acumulador, inicializado con un valor de `0`.
3. Divida la suma resultante entre la longitud del array.

A continuación, se muestra un fragmento de código de ejemplo que puede utilizar:

```js
const average = (...nums) =>
  nums.reduce((acc, val) => acc + val, 0) / nums.length;
```

Puede llamar a la función `average` con un array o múltiples argumentos:

```js
average(...[1, 2, 3]); // 2
average(1, 2, 3); // 2
```
