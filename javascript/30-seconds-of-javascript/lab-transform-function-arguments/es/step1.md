# Transformar los argumentos de una función

Para transformar los argumentos de una función, utiliza la función `overArgs`, que crea una nueva función que invoca la función proporcionada con sus argumentos transformados.

- Para transformar los argumentos, utiliza `Array.prototype.map()` en combinación con el operador de propagación (`...`) y pasa los argumentos transformados a `fn`.

```js
const overArgs =
  (fn, transforms) =>
  (...args) =>
    fn(...args.map((val, i) => transforms[i](val)));
```

- Para probar la función `overArgs`, crea una función de ejemplo y una matriz de transformaciones, luego llama a la nueva función con argumentos.

```js
const square = (n) => n * n;
const double = (n) => n * 2;

const fn = overArgs((x, y) => [x, y], [square, double]);
fn(9, 3); // [81, 6]
```

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.
