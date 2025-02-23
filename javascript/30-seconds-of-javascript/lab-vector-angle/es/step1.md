# Cálculo del Ángulo de un Vector

Para calcular el ángulo (theta) entre dos vectores, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.reduce()`, `Math.pow()` y `Math.sqrt()` para calcular la magnitud de cada vector y el producto escalar de los dos vectores.
3. Utilice `Math.acos()` para calcular el arcocoseno y obtener el valor de theta.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const vectorAngle = (x, y) => {
  let mX = Math.sqrt(x.reduce((acc, n) => acc + Math.pow(n, 2), 0));
  let mY = Math.sqrt(y.reduce((acc, n) => acc + Math.pow(n, 2), 0));
  return Math.acos(x.reduce((acc, n, i) => acc + n * y[i], 0) / (mX * mY));
};

vectorAngle([3, 4], [4, 3]); // 0.283794109208328
```

Esta función toma dos arrays (`x` e `y`) como argumentos y devuelve el ángulo (en radianes) entre ellos.
