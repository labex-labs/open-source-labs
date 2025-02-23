# Cómo Encontrar los Primeros N Coincidencias

Para encontrar los primeros `n` elementos que cumplen con ciertos criterios, utiliza la función `findFirstN`. Aquí está cómo:

1. Abre la Terminal/SSH.
2. Escribe `node` para comenzar a practicar la codificación.
3. Utiliza la función `findFirstN`, pasando el array en el que buscar, una función de coincidencia y el número de coincidencias a encontrar (si no se especifica, el valor predeterminado es 1).
4. La función `matcher` se ejecutará para cada elemento del `arr`, y si devuelve un valor verdadero, ese elemento se agregará al array de resultados.
5. Si el array `res` alcanza una longitud de `n`, la función devolverá el array de resultados.
6. Si no se encuentran coincidencias, se devolverá un array vacío.

Aquí está el código de la función `findFirstN`:

```js
const findFirstN = (arr, matcher, n = 1) => {
  let res = [];
  for (let i in arr) {
    const el = arr[i];
    const match = matcher(el, i, arr);
    if (match) res.push(el);
    if (res.length === n) return res;
  }
  return res;
};
```

Y aquí hay algunos ejemplos de cómo usarlo:

```js
findFirstN([1, 2, 4, 6], (n) => n % 2 === 0, 2); // [2, 4]
findFirstN([1, 2, 4, 6], (n) => n % 2 === 0, 5); // [2, 4, 6]
```
