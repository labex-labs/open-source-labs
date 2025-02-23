# Función para devolver cada elemento enésimo de un array

Para devolver cada elemento enésimo en un array, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `Array.prototype.filter()` para crear un nuevo array que contenga cada elemento enésimo de un array dado.
3. Utilice la siguiente función para implementar el paso anterior:

```js
const everyNth = (arr, nth) => arr.filter((e, i) => i % nth === nth - 1);
```

4. Para probar la función, use el siguiente código:

```js
everyNth([1, 2, 3, 4, 5, 6], 2); // [ 2, 4, 6 ]
```

Esto devolverá un nuevo array con cada segundo elemento del array de entrada.
