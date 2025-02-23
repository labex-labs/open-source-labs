# Función para Encontrar la Primera Clave que Coincide con una Prueba

Para encontrar la primera clave en un objeto que coincida con una función de prueba dada, use la función `findKey()`. Primero, obtenga todas las propiedades del objeto usando `Object.keys()`. Luego, aplique la función de prueba a cada par clave-valor usando `Array.prototype.find()`. La función de prueba debe tomar tres argumentos: el valor, la clave y el objeto. La función devuelve la primera clave que satisface la función de prueba o `undefined` si no se encuentra ninguna.

A continuación, se muestra una implementación de ejemplo de `findKey()`:

```js
const findKey = (obj, fn) =>
  Object.keys(obj).find((key) => fn(obj[key], key, obj));
```

Para usar `findKey()`, pase el objeto y la función de prueba como argumentos:

```js
findKey(
  {
    barney: { age: 36, active: true },
    fred: { age: 40, active: false },
    pebbles: { age: 1, active: true }
  },
  (x) => x["active"]
); // 'barney'
```

En este ejemplo, `findKey()` devuelve la primera clave en el objeto donde el valor de la propiedad `active` es `true`, que es `'barney'`.
