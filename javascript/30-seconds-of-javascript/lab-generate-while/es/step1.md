# Generador que Produce Valores Mientras una Condición Sea Verdadera

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`. Esto creará un generador que seguirá produciendo nuevos valores siempre que se cumpla la condición dada.

El generador se inicializa con un valor `seed`, que se utiliza para inicializar el `val` actual. Luego, se utiliza un bucle `while` para iterar mientras la función `condition` llamada con el `val` actual devuelva `true`.

La palabra clave `yield` se utiliza para devolver el `val` actual y, opcionalmente, recibir un nuevo valor de semilla, `nextSeed`. La función `next` se utiliza para calcular el siguiente valor a partir del `val` actual y el `nextSeed`.

```js
const generateWhile = function* (seed, condition, next) {
  let val = seed;
  let nextSeed = null;
  while (condition(val)) {
    nextSeed = yield val;
    val = next(val, nextSeed);
  }
  return val;
};
```

Para usar el generador, llámalo con las funciones `seed`, `condition` y `next`. Por ejemplo, llamar a `[...generateWhile(1, v => v <= 5, v => ++v)]` devolverá `[1, 2, 3, 4, 5]`.
