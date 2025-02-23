# Cómo encontrar el elemento más largo en una matriz

Para encontrar el elemento más largo en una matriz, abre la Terminal/SSH y escribe `node`. La función toma cualquier número de objetos iterables o objetos con una propiedad `length` y devuelve el más largo. Utiliza `Array.prototype.reduce()` para comparar la longitud de los objetos y encontrar el más largo. Si varios objetos tienen la misma longitud, la función devuelve el primero. Si no se proporcionan argumentos, devuelve `undefined`.

Aquí está el código:

```js
const longestItem = (...vals) =>
  vals.reduce((a, x) => (x.length > a.length ? x : a));
```

Puedes usar la función de la siguiente manera:

```js
longestItem("this", "is", "a", "testcase"); // 'testcase'
longestItem(...["a", "ab", "abc"]); // 'abc'
longestItem(...["a", "ab", "abc"], "abcd"); // 'abcd'
longestItem([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]); // [1, 2, 3, 4, 5]
longestItem([1, 2, 3], "foobar"); // 'foobar'
```
