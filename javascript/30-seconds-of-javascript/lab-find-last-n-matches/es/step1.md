# Instrucciones para encontrar las últimas N coincidencias

Para encontrar los últimos `n` elementos que coinciden con una cierta condición, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice la función `findLastN` proporcionada a continuación.
3. Proporcione una matriz `arr` y una función `matcher` que devuelva un valor verdadero para los elementos que desea coincidir.
4. Opcionalmente, también puede proporcionar el número `n` de coincidencias que desea devolver (el valor predeterminado es 1).
5. La función ejecutará la función `matcher` para cada elemento de `arr` utilizando un bucle `for`, comenzando desde el último elemento.
6. Si un elemento coincide con la condición `matcher`, se agregará al arreglo de resultados utilizando `Array.prototype.unshift()`, que agrega elementos al principio del arreglo.
7. Cuando la longitud del arreglo de resultados sea igual a `n`, la función devolverá los resultados.
8. Si no hay coincidencias o `n` es mayor que el número de coincidencias, se devolverá un arreglo vacío.

```js
const findLastN = (arr, matcher, n = 1) => {
  let res = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    const el = arr[i];
    const match = matcher(el, i, arr);
    if (match) res.unshift(el);
    if (res.length === n) return res;
  }
  return res;
};
```

A continuación, se presentan algunos ejemplos de cómo utilizar la función `findLastN`:

```js
findLastN([1, 2, 4, 6], (n) => n % 2 === 0, 2); // [4, 6]
findLastN([1, 2, 4, 6], (n) => n % 2 === 0, 5); // [2, 4, 6]
```
