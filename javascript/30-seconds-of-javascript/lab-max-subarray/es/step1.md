# Algoritmo del subarreglo máximo

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. Este algoritmo encuentra un subarreglo contiguo con la suma más grande dentro de un arreglo de números. Para implementar este algoritmo, sigue estos pasos:

- Utiliza un enfoque voraz para llevar un registro de la suma actual y el máximo actual, `maxSum`. Establece `maxSum` en `-Infinity` para asegurar que se retorne el valor negativo más alto, si todos los valores son negativos.
- Define variables para llevar un registro del índice de inicio máximo, `sMax`, índice de fin máximo, `eMax` e índice de inicio actual, `s`.
- Utiliza `Array.prototype.forEach()` para iterar sobre los valores y agrega el valor actual a la `sum`.
- Si la `sum` actual es mayor que `maxSum`, actualiza los valores de los índices y la `maxSum`.
- Si la `sum` es menor que `0`, reiníciala en `0` y actualiza el valor de `s` al siguiente índice.
- Utiliza `Array.prototype.slice()` para retornar el subarreglo indicado por las variables de índice.

Aquí está el código JavaScript del algoritmo:

```js
const maxSubarray = (...arr) => {
  let maxSum = -Infinity,
    sum = 0;
  let sMax = 0,
    eMax = arr.length - 1,
    s = 0;

  arr.forEach((n, i) => {
    sum += n;
    if (maxSum < sum) {
      maxSum = sum;
      sMax = s;
      eMax = i;
    }

    if (sum < 0) {
      sum = 0;
      s = i + 1;
    }
  });

  return arr.slice(sMax, eMax + 1);
};
```

Aquí está un ejemplo de cómo utilizar la función:

```js
maxSubarray(-2, 1, -3, 4, -1, 2, 1, -5, 4); // [4, -1, 2, 1]
```
