# Conversión de las claves de un objeto a minúsculas

Para convertir todas las claves de un objeto a minúsculas, sigue estos pasos:

1. Abre la Terminal/SSH para comenzar a practicar la codificación y escribe `node`.
2. Utiliza `Object.keys()` para obtener un array de las claves del objeto.
3. Utiliza `Array.prototype.reduce()` para mapear el array a un objeto.
4. Utiliza `String.prototype.toLowerCase()` para convertir las claves a minúsculas.

A continuación, se muestra un ejemplo de código que implementa estos pasos:

```js
const lowerize = (obj) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k.toLowerCase()] = obj[k];
    return acc;
  }, {});
```

Luego, puedes llamar a la función `lowerize()` con un objeto como argumento para obtener un nuevo objeto con todas las claves en minúsculas. Por ejemplo:

```js
lowerize({ Name: "John", Age: 22 }); // { name: 'John', age: 22 }
```
