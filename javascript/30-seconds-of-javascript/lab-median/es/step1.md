# Cómo calcular la mediana de una matriz de números

Para calcular la mediana de una matriz de números, siga estos pasos:

1. Encuentre el centro de la matriz.
2. Utilice `Array.prototype.sort()` para ordenar los valores.
3. Si `Array.prototype.length` es impar, devuelva el número en el punto medio. Si es par, devuelva el promedio de los dos números del medio.
4. Para comenzar a practicar la codificación y usar `node`, abra la Terminal/SSH y escriba `node`.

A continuación, se muestra un fragmento de código de ejemplo que implementa esta lógica:

```js
const median = (arr) => {
  const mid = Math.floor(arr.length / 2),
    nums = [...arr].sort((a, b) => a - b);
  return arr.length % 2 !== 0 ? nums[mid] : (nums[mid - 1] + nums[mid]) / 2;
};
```

Puede llamar a esta función con una matriz de números como se muestra a continuación:

```js
median([5, 6, 50, 1, -5]); // 5
```
