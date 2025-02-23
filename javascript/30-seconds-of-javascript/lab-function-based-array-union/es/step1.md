# Cómo encontrar la unión de dos arrays basada en una función

Para encontrar la unión de dos arrays basada en una función utilizando Node.js, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node`.
2. Utilice el siguiente código para crear un `Set` con todos los valores de `a` y los valores en `b` para los cuales el comparador no encuentra coincidencias en `a`, utilizando `Array.prototype.findIndex()`:

```js
const unionWith = (a, b, comp) =>
  Array.from(
    new Set([...a, ...b.filter((x) => a.findIndex((y) => comp(x, y)) === -1)])
  );
```

3. Llame a la función `unionWith` con tres argumentos: el primer array, el segundo array y la función comparadora.
4. La función devuelve cada elemento que existe al menos una vez en cualquiera de los dos arrays, utilizando la función comparadora proporcionada.
5. Aquí hay un ejemplo de llamada a la función `unionWith`:

```js
unionWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0, 3.9],
  (a, b) => Math.round(a) === Math.round(b)
);
// [1, 1.2, 1.5, 3, 0, 3.9]
```

Esto devolverá `[1, 1.2, 1.5, 3, 0, 3.9]` como la unión de los dos arrays.
