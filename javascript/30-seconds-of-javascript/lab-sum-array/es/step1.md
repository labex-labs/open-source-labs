# Así es como se encuentra la suma de un array

Para encontrar la suma de un array de números, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a codificar.
2. Utilice el método `Array.prototype.reduce()` para agregar cada valor a un acumulador, que debe inicializarse con un valor de `0`.
3. Aquí está el código que puede utilizar para encontrar la suma del array:

```js
const sum = (...arr) => [...arr].reduce((acc, val) => acc + val, 0);
```

4. Para probar la función `sum`, use los siguientes ejemplos de código:

```js
sum(1, 2, 3, 4); // 10
sum(...[1, 2, 3, 4]); // 10
```

Siguiendo estos pasos, puede encontrar fácilmente la suma de un array de números utilizando JavaScript.
