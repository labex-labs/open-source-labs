# Función para mapear las claves de un objeto

Para mapear las claves de un objeto utilizando una función proporcionada y generar un nuevo objeto, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Object.keys()` para iterar sobre las claves del objeto.
3. Utilice `Array.prototype.reduce()` para crear un nuevo objeto con los mismos valores y claves mapeadas utilizando la función proporcionada (`fn`).

A continuación, se muestra una implementación de ejemplo de la función `mapKeys`:

```js
const mapKeys = (obj, fn) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[fn(obj[k], k, obj)] = obj[k];
    return acc;
  }, {});
```

Puede probar la función con una entrada de ejemplo como esta:

```js
mapKeys({ a: 1, b: 2 }, (val, key) => key + val); // { a1: 1, b2: 2 }
```
