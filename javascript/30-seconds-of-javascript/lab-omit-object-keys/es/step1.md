# Eliminar claves de un objeto

Para eliminar claves específicas de un objeto, utiliza la función `omit` que toma un objeto y una matriz de claves a eliminar.

- El método `Object.keys()` se utiliza para obtener todas las claves del objeto
- Luego, el método `Array.prototype.filter()` se utiliza para eliminar las claves especificadas de la lista de claves
- Finalmente, `Array.prototype.reduce()` se utiliza para crear un nuevo objeto con los pares clave-valor restantes

```js
const omit = (obj, keysToRemove) =>
  Object.keys(obj)
    .filter((key) => !keysToRemove.includes(key))
    .reduce((newObj, key) => {
      newObj[key] = obj[key];
      return newObj;
    }, {});
```

Uso de ejemplo:

```js
omit({ a: 1, b: "2", c: 3 }, ["b"]); // { 'a': 1, 'c': 3 }
```
