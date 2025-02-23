# Función para Dividir una Matriz en Dos Grupos

Para utilizar esta función para dividir una matriz en dos grupos en función de los valores, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice la función `bifurcate()`, que divide los valores en dos grupos en función del resultado de la matriz `filter` dada.
3. Para implementar la función, utilice `Array.prototype.reduce()` y `Array.prototype.push()` para agregar elementos a los grupos, en función de la matriz `filter`.
4. Si `filter` tiene un valor verdadero para cualquier elemento, agréguelo al primer grupo; de lo contrario, agréguelo al segundo grupo.

A continuación, se muestra el código de la función `bifurcate()`:

```js
const bifurcate = (arr, filter) =>
  arr.reduce(
    (acc, val, i) => (acc[filter[i] ? 0 : 1].push(val), acc),
    [[], []]
  );
```

Puede llamar a la función `bifurcate()` con una matriz de valores y una matriz de filtro correspondiente para dividir los valores en dos grupos. Por ejemplo:

```js
bifurcate(["beep", "boop", "foo", "bar"], [true, true, false, true]);
// [ ['beep', 'boop', 'bar'], ['foo'] ]
```
