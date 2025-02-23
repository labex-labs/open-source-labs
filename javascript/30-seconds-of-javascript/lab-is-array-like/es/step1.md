# Comprobar si un valor es similar a un array

Para comprobar si un valor es similar a un array, siga estos pasos:

1. Abra la Terminal/SSH.
2. Escriba `node`.
3. Utilice el siguiente código para comprobar si el argumento proporcionado es iterable:

```js
const isArrayLike = (obj) =>
  obj != null && typeof obj[Symbol.iterator] === "function";
```

4. La función devolverá `true` si el argumento proporcionado es un objeto similar a un array, y `false` en caso contrario.
5. Por ejemplo:

```js
isArrayLike([1, 2, 3]); // true
isArrayLike(document.querySelectorAll(".className")); // true
isArrayLike("abc"); // true
isArrayLike(null); // false
```
