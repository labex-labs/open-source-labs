# Función para mapear valores de objeto

Para mapear los valores de un objeto utilizando una función proporcionada para generar un nuevo objeto con las mismas claves, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Object.keys()` para iterar sobre las claves del objeto.
3. Utilice `Array.prototype.reduce()` para crear un nuevo objeto con las mismas claves y valores mapeados utilizando la función `fn` proporcionada.
4. El código siguiente demuestra la implementación de la función `mapValues`.

```js
const mapValues = (obj, fn) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k] = fn(obj[k], k, obj);
    return acc;
  }, {});
```

A continuación, se muestra un ejemplo de uso de la función `mapValues`:

```js
const users = {
  fred: { user: "fred", age: 40 },
  pebbles: { user: "pebbles", age: 1 }
};
mapValues(users, (u) => u.age); // { fred: 40, pebbles: 1 }
```
