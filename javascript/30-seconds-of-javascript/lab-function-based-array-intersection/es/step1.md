# Cómo encontrar la intersección de arrays basada en una función usando JavaScript

Para encontrar los elementos que existen en ambos arrays basados en una función comparadora proporcionada, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.

2. Utilice `Array.prototype.filter()` y `Array.prototype.findIndex()` en combinación con la función comparadora proporcionada para determinar los valores en común.

   ```js
   const intersectionWith = (a, b, comp) =>
     a.filter((x) => b.findIndex((y) => comp(x, y)) !== -1);
   ```

3. Llame a la función `intersectionWith()` con los dos arrays y la función comparadora como argumentos.

   ```js
   intersectionWith(
     [1, 1.2, 1.5, 3, 0],
     [1.9, 3, 0, 3.9],
     (a, b) => Math.round(a) === Math.round(b)
   ); // [1.5, 3, 0]
   ```

Esto devolverá un array que contiene los valores en común entre los dos arrays, basados en la función comparadora proporcionada.
