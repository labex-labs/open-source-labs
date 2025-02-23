# Cómo contar subcadenas en una cadena de texto con JavaScript

Si quieres practicar la programación, abre la Terminal/SSH y escribe `node`. Esta función de JavaScript cuenta el número de veces que aparece una subcadena especificada en una cadena de texto dada.

Para utilizar esta función, sigue estos pasos:

1. Declara una función llamada `countSubstrings` que tome dos parámetros: `str` y `searchValue`.
2. Inicializa dos variables: `count` e `i`.
3. Utiliza el método `Array.prototype.indexOf()` para buscar `searchValue` en `str`.
4. Si se encuentra el valor, incrementa la variable `count` y actualiza la variable `i`.
5. Utiliza un bucle `while` que devuelva tan pronto como el valor devuelto por `Array.prototype.indexOf()` sea `-1`.
6. Devuelve la variable `count`.

Aquí está el código de la función `countSubstrings`:

```js
const countSubstrings = (str, searchValue) => {
  let count = 0,
    i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) [count, i] = [count + 1, r + 1];
    else return count;
  }
};
```

Puedes probar la función con los ejemplos siguientes:

```js
countSubstrings("tiktok tok tok tik tok tik", "tik"); // 3
countSubstrings("tutut tut tut", "tut"); // 4
```
