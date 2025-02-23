# Medir el Tiempo que Tarda una Función

Para medir el tiempo que tarda una función, utiliza `console.time()` y `console.timeEnd()` para determinar la diferencia entre los tiempos de inicio y finalización.

A continuación, se muestra una función de ejemplo llamada `timeTaken` que mide el tiempo que tarda una función de devolución de llamada:

```js
const timeTaken = (callback) => {
  console.time("timeTaken");
  const result = callback();
  console.timeEnd("timeTaken");
  return result;
};
```

Para utilizar esta función, simplemente pasa tu función de devolución de llamada como argumento. Por ejemplo:

```js
timeTaken(() => Math.pow(2, 10)); // Devuelve 1024, y registra: timeTaken: 0.02099609375ms
```

En el ejemplo anterior, la función `timeTaken` se utiliza para medir el tiempo que tarda en ejecutarse la llamada a la función `Math.pow(2, 10)`, que devuelve 1024. La salida de la consola mostrará el tiempo transcurrido en milisegundos (ms).
