# Generando números primos utilizando el Criba de Eratóstenes

Para generar números primos hasta un número dado utilizando el Criba de Eratóstenes, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Crea una matriz que contenga números del `2` hasta el número dado.
3. Utiliza `Array.prototype.filter()` para filtrar los valores que son divisibles por cualquier número del `2` hasta la raíz cuadrada del número proporcionado.
4. Devuelve la matriz resultante que contiene números primos.

Aquí está el código de JavaScript para generar números primos hasta un número dado:

```js
const generatePrimes = (num) => {
  let arr = Array.from({ length: num - 1 }).map((x, i) => i + 2),
    sqrt = Math.floor(Math.sqrt(num)),
    numsTillSqrt = Array.from({ length: sqrt - 1 }).map((x, i) => i + 2);
  numsTillSqrt.forEach(
    (x) => (arr = arr.filter((y) => y % x !== 0 || y === x))
  );
  return arr;
};
```

Puedes llamar a la función `generatePrimes()` pasando el número deseado como argumento. Por ejemplo:

```js
generatePrimes(10); // [2, 3, 5, 7]
```
