# Composición de funciones con tuberías

Para comenzar a practicar la codificación con tuberías, abre la Terminal/SSH y escribe `node`.

La función `pipeFunctions` realiza la composición de funciones de izquierda a derecha utilizando `Array.prototype.reduce()` con el operador de propagación (`...`). La primera (más a la izquierda) función puede aceptar uno o más argumentos, mientras que las funciones restantes deben ser unarias.

```js
const pipeFunctions = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args))
  );
```

Aquí hay un ejemplo de cómo usar `pipeFunctions` para crear una nueva función `multiplyAndAdd5` que multiplica dos números y luego suma 5 al resultado:

```js
const add5 = (x) => x + 5;
const multiply = (x, y) => x * y;
const multiplyAndAdd5 = pipeFunctions(multiply, add5);
multiplyAndAdd5(5, 2); // 15
```

En este ejemplo, `multiplyAndAdd5` es una nueva función que toma dos argumentos, `5` y `2`, y aplica primero `multiply` a ellos, lo que da como resultado `10`, y luego aplica `add5` al resultado, lo que da como resultado `15`.
