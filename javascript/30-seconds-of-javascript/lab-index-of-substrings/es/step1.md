# Índice de Subcadenas

Para encontrar todos los índices de una subcadena en una cadena dada, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método integrado `Array.prototype.indexOf()` para buscar `searchValue` en `str`.
3. Utilice `yield` para devolver el índice si se encuentra el valor y actualice el índice, `i`.
4. Utilice un bucle `while` que terminará el generador tan pronto como el valor devuelto por `Array.prototype.indexOf()` sea `-1`.

A continuación, se muestra un código de ejemplo para implementar los pasos anteriores:

```js
const indexOfSubstrings = function* (str, searchValue) {
  let i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) {
      yield r;
      i = r + 1;
    } else return;
  }
};
```

Puede probar la función con el siguiente código:

```js
[...indexOfSubstrings("tiktok tok tok tik tok tik", "tik")]; // [0, 15, 23]
[...indexOfSubstrings("tutut tut tut", "tut")]; // [0, 2, 6, 10]
[...indexOfSubstrings("hello", "hi")]; // []
```
