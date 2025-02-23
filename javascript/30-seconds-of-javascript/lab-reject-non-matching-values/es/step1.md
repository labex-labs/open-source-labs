# Filtrado de valores de array

Para filtrar un array en función de una función predicado y devolver solo los valores para los cuales la función predicado devuelve `false`, siga estos pasos:

1. Utilice `Array.prototype.filter()` en combinación con la función predicado, `pred`.
2. El método `filter` devolverá solo los valores para los cuales la función predicado devuelve `false`.
3. Para rechazar los valores que no coinciden, pase la función predicado y el array a la función `reject()`.

```js
const reject = (pred, array) => array.filter((...args) => !pred(...args));
```

A continuación, se presentan algunos ejemplos de cómo utilizar la función `reject()`:

```js
reject((x) => x % 2 === 0, [1, 2, 3, 4, 5]); // [1, 3, 5]
reject((word) => word.length > 4, ["Apple", "Pear", "Kiwi", "Banana"]);
// ['Pear', 'Kiwi']
```

Siguiendo estos pasos, puede filtrar fácilmente un array en función de una función predicado y rechazar los valores que no coinciden.
