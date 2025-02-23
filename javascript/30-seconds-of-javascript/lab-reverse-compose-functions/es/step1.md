# Reversión de la composición de funciones

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Aquí está cómo realizar la composición de funciones de izquierda a derecha:

- Utiliza el método `Array.prototype.reduce()` para realizar la composición de funciones de izquierda a derecha.
- La primera (más a la izquierda) función puede aceptar uno o más argumentos, mientras que las funciones restantes deben ser unarias.

```js
const composeRight = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args))
  );
```

Por ejemplo:

```js
const add = (x, y) => x + y;
const square = (x) => x * x;
const addAndSquare = composeRight(add, square);
addAndSquare(1, 2); // 9
```
