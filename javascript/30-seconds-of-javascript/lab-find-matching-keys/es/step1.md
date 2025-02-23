# Encontrar claves coincidentes

Para encontrar todas las claves en un objeto que coincidan con un valor dado, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Object.keys()` para obtener todas las propiedades del objeto.
3. Utilice `Array.prototype.filter()` para probar cada par clave-valor y devolver todas las claves que son iguales al valor dado.

A continuación, se muestra una función de ejemplo que implementa esta lógica:

```js
const findKeys = (obj, val) =>
  Object.keys(obj).filter((key) => obj[key] === val);
```

Puede usar esta función de la siguiente manera:

```js
const ages = {
  Leo: 20,
  Zoey: 21,
  Jane: 20
};
findKeys(ages, 20); // [ 'Leo', 'Jane' ]
```
