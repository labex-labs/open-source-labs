# Desviación estándar

Para calcular la desviación estándar de una matriz de números en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice la función `standardDeviation(arr, usePopulation = false)` proporcionada a continuación.
3. Pase una matriz de números como primer argumento a la función.
4. Omita el segundo argumento, `usePopulation`, para obtener la desviación estándar de muestra. Establezcalo en `true` para obtener la desviación estándar de población.

```js
const standardDeviation = (arr, usePopulation = false) => {
  const mean = arr.reduce((acc, val) => acc + val, 0) / arr.length;
  return Math.sqrt(
    arr
      .reduce((acc, val) => acc.concat((val - mean) ** 2), [])
      .reduce((acc, val) => acc + val, 0) /
      (arr.length - (usePopulation ? 0 : 1))
  );
};
```

Uso de ejemplo:

```js
standardDeviation([10, 2, 38, 23, 38, 23, 21]); // 13.284434142114991 (muestra)
standardDeviation([10, 2, 38, 23, 38, 23, 21], true); // 12.29899614287479 (población)
```
