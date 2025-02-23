# Cómo obtener los últimos N elementos de una matriz en JavaScript

Para obtener los últimos `n` elementos de una matriz en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.

2. Utilice `Array.prototype.slice()` con un valor de inicio de `-n` para obtener los últimos `n` elementos de la matriz.

Aquí está el código de JavaScript para obtener los últimos `n` elementos de una matriz:

```js
const lastN = (arr, n) => arr.slice(-n);
```

Para probar el código, llame a la función `lastN()` con la matriz y el número de elementos que desea obtener, como se muestra a continuación:

```js
lastN(["a", "b", "c", "d"], 2); // ['c', 'd']
```
