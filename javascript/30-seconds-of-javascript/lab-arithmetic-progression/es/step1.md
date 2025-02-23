# Ejemplo de código de progresión aritmética

Para practicar la codificación, abre la Terminal/SSH y escribe `node`.

A continuación, se presenta un ejemplo de código que crea una matriz de números en progresión aritmética. La matriz comienza con un número entero positivo dado y va hasta un límite especificado:

```js
const arithmeticProgression = (n, lim) =>
  Array.from({ length: Math.ceil(lim / n) }, (_, i) => (i + 1) * n);
```

Para usar este código, simplemente llama a la función `arithmeticProgression` con dos argumentos: el número entero positivo inicial y el límite. Por ejemplo:

```js
arithmeticProgression(5, 25); // [5, 10, 15, 20, 25]
```
