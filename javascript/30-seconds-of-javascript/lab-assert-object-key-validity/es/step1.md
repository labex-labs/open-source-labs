# Validar claves de objeto

Para asegurarse de que todas las claves de un objeto coincidan con las `keys` especificadas, siga estos pasos:

- Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
- Utilice `Object.keys()` para recuperar las claves del objeto, `obj`.
- Utilice `Array.prototype.every()` y `Array.prototype.includes()` para validar que cada clave del objeto está incluida en el array `keys`.

A continuación, se muestra una implementación de ejemplo:

```js
const validateObjectKeys = (obj, keys) =>
  Object.keys(obj).every((key) => keys.includes(key));
```

Puede usar la función de la siguiente manera:

```js
validateObjectKeys({ id: 10, name: "apple" }, ["id", "name"]); // true
validateObjectKeys({ id: 10, name: "apple" }, ["id", "type"]); // false
```
