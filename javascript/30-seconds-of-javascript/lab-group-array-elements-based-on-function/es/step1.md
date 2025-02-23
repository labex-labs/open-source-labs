# Función de JavaScript para agrupar elementos de un array

Para agrupar elementos en arrays, puedes utilizar la función `zipWith`.

Aquí cómo funciona:

- La función toma un número ilimitado de arrays como argumentos.
- Verifica si el último argumento es una función.
- Utiliza `Math.max()` para encontrar la longitud del array más largo.
- Crea un nuevo array de elementos agrupados utilizando `Array.from()` y una función de mapeo.
- Si las longitudes de los arrays de argumentos varían, se utiliza `undefined` donde no se puede encontrar un valor.
- La función se invoca con los elementos de cada grupo.

Aquí un ejemplo de uso de la función `zipWith`:

```js
zipWith([1, 2], [10, 20], [100, 200], (a, b, c) => a + b + c); // [111, 222]
zipWith(
  [1, 2, 3],
  [10, 20],
  [100, 200],
  (a, b, c) =>
    (a != null ? a : "a") + (b != null ? b : "b") + (c != null ? c : "c")
); // [111, 222, '3bc']
```

Para utilizar la función `zipWith`, abre la Terminal/SSH y escribe `node`.
