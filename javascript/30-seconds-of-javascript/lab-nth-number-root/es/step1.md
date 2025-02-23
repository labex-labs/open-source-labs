# Cómo calcular la raíz n-ésima de un número

Para calcular la raíz n-ésima de un número:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice la fórmula `Math.pow(x, 1/n)` para calcular `x` elevado a la potencia de `1/n`.
3. El resultado de este cálculo es igual a la raíz n-ésima de `x`.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const nthRoot = (x, n) => Math.pow(x, 1 / n);
nthRoot(32, 5); // Salida: 2
```

Este código calculará la raíz n-ésima de 32 (donde n es 5) y devolverá la salida como 2.
