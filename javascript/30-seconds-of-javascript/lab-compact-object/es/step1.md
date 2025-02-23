# Algoritmo para objeto compacto

Para eliminar profundamente todos los valores falsos de un objeto o matriz, utilice el siguiente algoritmo:

1. Utilice la recursividad para llamar a la función `compactObject()` en cada objeto o matriz anidada.
2. Inicialice los datos iterables utilizando `Array.isArray()`, `Array.prototype.filter()` y `Boolean()`. Esto se hace para evitar matrices dispersas.
3. Utilice `Object.keys()` y `Array.prototype.reduce()` para iterar sobre cada clave con un valor inicial adecuado.
4. Utilice `Boolean()` para determinar la verdadera validez del valor de cada clave y agréguelo al acumulador si es verdadero.
5. Utilice `typeof` para determinar si un valor dado es un `object` y llame a la función nuevamente para compactarlo profundamente.

Aquí está el código para la función `compactObject()`:

```js
const compactObject = (val) => {
  const data = Array.isArray(val) ? val.filter(Boolean) : val;
  return Object.keys(data).reduce(
    (acc, key) => {
      const value = data[key];
      if (Boolean(value))
        acc[key] = typeof value === "object" ? compactObject(value) : value;
      return acc;
    },
    Array.isArray(val) ? [] : {}
  );
};
```

Para utilizar esta función, pase un objeto o matriz como argumento a `compactObject()`. La función devolverá un nuevo objeto o matriz con todos los valores falsos eliminados.

Por ejemplo:

```js
const obj = {
  a: null,
  b: false,
  c: true,
  d: 0,
  e: 1,
  f: "",
  g: "a",
  h: [null, false, "", true, 1, "a"],
  i: { j: 0, k: false, l: "a" }
};
compactObject(obj);
// { c: true, e: 1, g: 'a', h: [ true, 1, 'a' ], i: { l: 'a' } }
```
