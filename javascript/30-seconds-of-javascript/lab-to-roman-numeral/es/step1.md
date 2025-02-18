# Conversión de números enteros a números romanos

Para convertir un número entero a su representación en números romanos, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.

2. La función `toRomanNumeral()` acepta valores entre `1` y `3999` (ambos inclusive).

3. Crea una tabla de búsqueda que contenga arreglos de dos valores en la forma de (valor romano, entero).

4. Utiliza `Array.prototype.reduce()` para recorrer los valores en `lookup` y dividir repetidamente `num` por el valor.

5. Utiliza `String.prototype.repeat()` para agregar la representación en números romanos al acumulador.

Aquí está el código de la función `toRomanNumeral()`:

```js
const toRomanNumeral = (num) => {
  const lookup = [
    ["M", 1000],
    ["CM", 900],
    ["D", 500],
    ["CD", 400],
    ["C", 100],
    ["XC", 90],
    ["L", 50],
    ["XL", 40],
    ["X", 10],
    ["IX", 9],
    ["V", 5],
    ["IV", 4],
    ["I", 1]
  ];
  return lookup.reduce((acc, [k, v]) => {
    acc += k.repeat(Math.floor(num / v));
    num = num % v;
    return acc;
  }, "");
};
```

Puedes probar la función con estos ejemplos:

```js
toRomanNumeral(3); // 'III'
toRomanNumeral(11); // 'XI'
toRomanNumeral(1998); // 'MCMXCVIII'
```
