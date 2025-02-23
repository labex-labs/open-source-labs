# Verificación de Luhn

Para usar el Algoritmo de Luhn para la validación de números de identificación, como números de tarjeta de crédito, números IMEI, números de Identificador Nacional de Proveedor, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice los siguientes métodos: `String.prototype.split()`, `Array.prototype.reverse()`, `Array.prototype.map()` y `parseInt()` en combinación para obtener una matriz de dígitos.
3. Utilice `Array.prototype.shift()` para obtener el último dígito.
4. Utilice `Array.prototype.reduce()` para implementar el Algoritmo de Luhn.
5. Devuelva `true` si `sum` es divisible por `10`, `false` en caso contrario.

Aquí está el código:

```js
const luhnCheck = (num) => {
  const arr = (num + "")
    .split("")
    .reverse()
    .map((x) => parseInt(x));
  const lastDigit = arr.shift();
  let sum = arr.reduce(
    (acc, val, i) =>
      i % 2 !== 0 ? acc + val : acc + ((val *= 2) > 9 ? val - 9 : val),
    0
  );
  sum += lastDigit;
  return sum % 10 === 0;
};
```

Puede probar la función de verificación de Luhn con estos ejemplos:

```js
luhnCheck("4485275742308327"); // true
luhnCheck(6011329933655299); //  true
luhnCheck(123456789); // false
```
