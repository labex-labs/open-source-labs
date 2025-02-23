# Cómo obtener los primeros N elementos de un array en JavaScript

Para obtener los primeros `n` elementos de un array en JavaScript, puedes usar el método `Array.prototype.slice()`. Aquí está cómo:

```js
const firstN = (arr, n) => arr.slice(0, n);
```

En este fragmento de código, `arr` representa el array del que quieres extraer los elementos, y `n` representa el número de elementos que quieres extraer. El método `slice()` toma dos argumentos: el índice de inicio (que es `0` en este caso) y el índice de fin (que es `n`). El método devuelve un nuevo array que contiene los elementos extraídos.

Aquí hay un ejemplo de cómo usar la función `firstN()`:

```js
firstN(["a", "b", "c", "d"], 2); // ['a', 'b']
```

Esto devolverá los primeros dos elementos del array `['a', 'b', 'c', 'd']`, que son `['a', 'b']`.
