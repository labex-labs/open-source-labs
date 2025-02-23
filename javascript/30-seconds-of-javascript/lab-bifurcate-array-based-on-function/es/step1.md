# Función para Dividir un Arreglo en Dos Grupos

Para dividir un arreglo en dos grupos basado en el resultado de una función dada, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice los métodos `Array.prototype.reduce()` y `Array.prototype.push()` para agregar elementos a los grupos. Esto se basa en el valor devuelto por la función `fn` dada para cada elemento.
3. Si `fn` devuelve un valor verdadero para cualquier elemento, agréguelo al primer grupo. De lo contrario, agréguelo al segundo grupo.

Aquí está el código:

```js
const bifurcateBy = (arr, fn) =>
  arr.reduce(
    (acc, val, i) => (acc[fn(val, i) ? 0 : 1].push(val), acc),
    [[], []]
  );
```

Por ejemplo, si llama a `bifurcateBy(['beep', 'boop', 'foo', 'bar'], x => x[0] === 'b')`, la función devolverá `[ ['beep', 'boop', 'bar'], ['foo'] ]`.
