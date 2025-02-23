# Convertir una matriz en un objeto basado en una clave específica

Para convertir una matriz en un objeto basado en una clave específica y excluir esa clave de cada valor, siga estos pasos:

- Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
- Utilice `Array.prototype.reduce()` para crear un objeto a partir de la matriz proporcionada.
- Utilice la extracción de objetos para extraer el valor de la `clave` dada y los datos asociados, y luego agregue el par clave-valor al objeto.

A continuación, se muestra una implementación de ejemplo:

```js
const indexOn = (arr, key) =>
  arr.reduce((obj, v) => {
    const { [key]: id, ...data } = v;
    obj[id] = data;
    return obj;
  }, {});
```

Luego, puede usar la función de la siguiente manera:

```js
indexOn(
  [
    { id: 10, name: "apple" },
    { id: 20, name: "orange" }
  ],
  "id"
);
// { '10': { name: 'apple' }, '20': { name: 'orange' } }
```
