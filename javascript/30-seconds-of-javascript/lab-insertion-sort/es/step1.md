# Algoritmo de ordenamiento por inserción en JavaScript

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. Este algoritmo ordena una matriz de números utilizando el método de ordenamiento por inserción. Sigue estos pasos para implementar este algoritmo:

1. Utiliza `Array.prototype.reduce()` para iterar sobre todos los elementos en la matriz dada.
2. Si la `longitud` del acumulador es `0`, agrega el elemento actual a él.
3. Utiliza `Array.prototype.some()` para iterar sobre los resultados en el acumulador hasta que se encuentre la posición correcta.
4. Utiliza `Array.prototype.splice()` para insertar el elemento actual en el acumulador.

Aquí está el código para implementar el ordenamiento por inserción en JavaScript:

```js
const insertionSort = (arr) =>
  arr.reduce((acc, x) => {
    if (!acc.length) return [x];
    acc.some((y, j) => {
      if (x <= y) {
        acc.splice(j, 0, x);
        return true;
      }
      if (x > y && j === acc.length - 1) {
        acc.splice(j + 1, 0, x);
        return true;
      }
      return false;
    });
    return acc;
  }, []);
```

Puedes probar el algoritmo con el siguiente código:

```js
insertionSort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
