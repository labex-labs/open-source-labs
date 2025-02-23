# Cálculo de la Distancia de Hamming

Para calcular la distancia de Hamming entre dos valores, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el operador XOR (`^`) para encontrar la diferencia de bits entre los dos números.
3. Convierta el resultado a una cadena binaria utilizando `Number.prototype.toString()`.
4. Cuente el número de `1`s en la cadena utilizando `String.prototype.match()`.
5. Devuelva el recuento.

Aquí está el código para la función `hammingDistance`:

```js
const hammingDistance = (num1, num2) =>
  ((num1 ^ num2).toString(2).match(/1/g) || "").length;
```

Puede probar la función ejecutando `hammingDistance(2, 3); // 1`.
