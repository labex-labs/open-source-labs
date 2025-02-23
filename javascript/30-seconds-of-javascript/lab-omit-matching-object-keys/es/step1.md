# Eliminación de claves de objeto basadas en una función de devolución de llamada

Para eliminar claves de objeto basadas en una función de devolución de llamada, utiliza la función `omitBy`.

- `omitBy` crea un objeto que consta de propiedades que devuelven valores falsy para la función dada.
- `Object.keys()` y `Array.prototype.filter()` se utilizan para eliminar las claves para las cuales `fn` devuelve un valor truthy.
- `Array.prototype.reduce()` convierte las claves filtradas de nuevo en un objeto con los pares de clave-valor correspondientes.
- La función de devolución de llamada toma dos argumentos: `value` y `key`.
- El ejemplo siguiente muestra cómo se utiliza `omitBy` para eliminar las claves numéricas de un objeto.

```js
const omitBy = (obj, fn) =>
  Object.keys(obj)
    .filter((k) => !fn(obj[k], k))
    .reduce((acc, key) => ((acc[key] = obj[key]), acc), {});

omitBy({ a: 1, b: "2", c: 3 }, (x) => typeof x === "number"); // { b: '2' }
```
