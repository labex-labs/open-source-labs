# Cálculo de la frecuencia de una función

Para medir la frecuencia de ejecución de una función por segundo (hz/hertz), utiliza la función `hz`. Puedes hacerlo siguiendo estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `performance.now()` para obtener la diferencia en milisegundos antes y después del bucle de iteración para calcular el tiempo transcurrido al ejecutar la función `iteraciones` veces.
3. Convierte los milisegundos a segundos y divídelo por el tiempo transcurrido para devolver el número de ciclos por segundo.
4. Si quieres utilizar el valor predeterminado de 100 iteraciones, omite el segundo argumento, `iteraciones`.

```js
const hz = (fn, iterations = 100) => {
  const before = performance.now();
  for (let i = 0; i < iterations; i++) fn();
  return (1000 * iterations) / (performance.now() - before);
};
```

A continuación, se muestra un ejemplo de uso de la función `hz` para comparar el rendimiento de dos funciones que calculan la suma de una matriz de 10.000 números:

```js
const numbers = Array(10000)
  .fill()
  .map((_, i) => i);

const sumReduce = () => numbers.reduce((acc, n) => acc + n, 0);
const sumForLoop = () => {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) sum += numbers[i];
  return sum;
};

Math.round(hz(sumReduce)); // 572
Math.round(hz(sumForLoop)); // 4784
```

En este ejemplo, `sumReduce` es más rápido que `sumForLoop` porque tiene una frecuencia de ejecución de función más baja.
