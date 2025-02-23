# Función de verificación de valores verdaderos en una colección

Para practicar la codificación, escriba `node` en la Terminal/SSH.

A continuación, se presenta una función que verifica si una función predicado es verdadera para todos los elementos de una colección.

- Utilice `Array.prototype.every()` para comprobar si cada objeto pasado tiene la propiedad especificada y si devuelve un valor verdadero.

```js
const truthCheckCollection = (collection, pre) =>
  collection.every((obj) => obj[pre]);
```

Uso de ejemplo:

```js
truthCheckCollection(
  [
    { user: "Tinky-Winky", sex: "male" },
    { user: "Dipsy", sex: "male" }
  ],
  "sex"
); // true
```
