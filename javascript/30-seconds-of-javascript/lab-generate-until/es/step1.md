# Generando valores hasta que se cumpla una condición dada

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`. Una vez que hayas hecho eso, puedes crear un generador que produzca nuevos valores hasta que se cumpla una condición dada.

Para crear este generador, sigue estos pasos:

- Inicializa el `val` actual utilizando el valor `seed`.
- Utiliza un bucle `while` para seguir iterando mientras la función `condition`, llamada con el `val` actual, devuelva `false`.
- Utiliza la palabra clave `yield` para devolver el `val` actual y, opcionalmente, recibir un nuevo valor `seed`, `nextSeed`.
- Utiliza la función `next` para calcular el siguiente valor a partir del `val` actual y el `nextSeed`.

Aquí hay un fragmento de código de ejemplo:

```js
const generateUntil = function* (seed, condition, next) {
  let val = seed;
  let nextSeed = null;
  while (!condition(val)) {
    nextSeed = yield val;
    val = next(val, nextSeed);
  }
  return val;
};
```

Puedes utilizar el generador llamándolo con los argumentos adecuados. Por ejemplo:

```js
[
  ...generateUntil(
    1,
    (v) => v > 5,
    (v) => ++v
  )
]; // [1, 2, 3, 4, 5]
```

Esto producirá una matriz de valores de `1` a `5`, ya que la condición `v > 5` se cumple cuando `val` es igual a `6`.
