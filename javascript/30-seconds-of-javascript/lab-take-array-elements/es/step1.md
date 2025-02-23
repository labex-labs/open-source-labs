# Cómo eliminar elementos de una matriz en JavaScript

Para eliminar elementos desde el principio de una matriz en JavaScript, siga estos pasos:

1. Abra la Terminal o SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `Array.prototype.slice()` para crear una nueva matriz con `n` elementos eliminados desde el principio.
3. Utilice la función `take` en el siguiente fragmento de código para implementar la lógica.

```js
const take = (arr, n = 1) => arr.slice(0, n);
```

Aquí hay un ejemplo de cómo utilizar la función `take`:

```js
take([1, 2, 3], 5); // [1, 2, 3]
take([1, 2, 3], 0); // []
```

En el primer ejemplo, `take([1, 2, 3], 5)` devuelve `[1, 2, 3]` porque solo hay 3 elementos en la matriz. En el segundo ejemplo, `take([1, 2, 3], 0)` devuelve `[]` porque no se toman elementos desde el principio de la matriz.
