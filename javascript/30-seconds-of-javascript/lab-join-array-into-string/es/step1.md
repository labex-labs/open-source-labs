# Cómo unir una matriz en una cadena

Para unir todos los elementos de una matriz en una cadena, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza la función `join()` con los siguientes parámetros:
   - `arr`: la matriz que se va a unir.
   - `separator` (opcional): el separador que se utilizará entre los elementos de la matriz. Si no se especifica, se utilizará el separador predeterminado `,`.
   - `end` (opcional): el separador que se utilizará entre los últimos dos elementos de la matriz. Si no se especifica, se utilizará el mismo valor que `separator` por defecto.
3. La función `join()` utiliza `Array.prototype.reduce()` para combinar los elementos de la matriz en una cadena.
4. Se devuelve la cadena final.

Aquí está el código de la función `join()`:

```js
const join = (arr, separator = ",", end = separator) =>
  arr.reduce(
    (acc, val, i) =>
      i === arr.length - 2
        ? acc + val + end
        : i === arr.length - 1
          ? acc + val
          : acc + val + separator,
    ""
  );
```

Y aquí hay algunos ejemplos de cómo utilizar la función `join()`:

```js
join(["pen", "pineapple", "apple", "pen"], ",", "&"); // 'pen,pineapple,apple&pen'
join(["pen", "pineapple", "apple", "pen"], ","); // 'pen,pineapple,apple,pen'
join(["pen", "pineapple", "apple", "pen"]); // 'pen,pineapple,apple,pen'
```
