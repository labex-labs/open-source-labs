# Cómo convertir las claves de un objeto a mayúsculas en JavaScript

Para convertir todas las claves de un objeto a mayúsculas en JavaScript, sigue estos pasos:

1. Utiliza `Object.keys()` para obtener un array con las claves del objeto.
2. Utiliza `Array.prototype.reduce()` para mapear el array a un objeto.
3. Utiliza `String.prototype.toUpperCase()` para convertir las claves a mayúsculas.

Aquí está el código:

```js
const upperize = (obj) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k.toUpperCase()] = obj[k];
    return acc;
  }, {});
```

Para probar la función, puedes llamarla de la siguiente manera:

```js
upperize({ Name: "John", Age: 22 }); // { NAME: 'John', AGE: 22 }
```
