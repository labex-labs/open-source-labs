# Práctica de código: Cociente y módulo de la división

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. Este código devuelve una matriz que consta del cociente y el residuo de los números dados.

Para obtener el cociente de la división `x / y`, utiliza `Math.floor()`. Para obtener el residuo de la división `x / y`, utiliza el operador módulo (`%`).

```js
const divmod = (x, y) => [Math.floor(x / y), x % y];
```

Por ejemplo:

```js
divmod(8, 3); // [2, 2]
divmod(3, 8); // [0, 3]
divmod(5, 5); // [1, 0]
```
