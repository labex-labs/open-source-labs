# Cómo renombrar las claves de un objeto en JavaScript

Para renombrar múltiples claves de un objeto con los valores proporcionados, puedes usar la función `renameKeys`. Aquí están los pasos que debes seguir:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `Object.keys()` en combinación con `Array.prototype.reduce()` y el operador de propagación (`...`) para obtener las claves del objeto y renombrarlas de acuerdo con `keysMap`.
3. Pasa `keysMap` y el objeto (`obj`) como argumentos a la función `renameKeys`.
4. La función `renameKeys` devuelve un nuevo objeto con las claves renombradas.

Aquí hay un ejemplo de cómo usar la función `renameKeys`:

```js
const renameKeys = (keysMap, obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({
      ...acc,
      ...{ [keysMap[key] || key]: obj[key] }
    }),
    {}
  );

const obj = { name: "Bobo", job: "Front-End Master", shoeSize: 100 };
renameKeys({ name: "firstName", job: "passion" }, obj);
// { firstName: 'Bobo', passion: 'Front-End Master', shoeSize: 100 }
```
