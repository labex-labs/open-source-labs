# Convertir un iterable en un hash

Para convertir un iterable (objeto o matriz) en un hash (almacén de datos con claves), siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Object.values()` para obtener los valores del iterable.
3. Utilice `Array.prototype.reduce()` para iterar sobre los valores y crear un objeto que tenga como clave el valor de referencia.
4. Llame a la función `toHash` con el iterable y un parámetro de clave opcional para especificar el valor de referencia.

A continuación, se muestra una implementación de ejemplo de la función `toHash` en JavaScript:

```js
const toHash = (iterable, key) =>
  Object.values(iterable).reduce((acc, data, index) => {
    acc[!key ? index : data[key]] = data;
    return acc;
  }, {});
```

Puede llamar a la función `toHash` con diferentes iterables y claves para crear diferentes hashes. Por ejemplo:

```js
toHash([4, 3, 2, 1]); // { 0: 4, 1: 3, 2: 2, 3: 1 }
toHash([{ a: "label" }], "a"); // { label: { a: 'label' } }
```
