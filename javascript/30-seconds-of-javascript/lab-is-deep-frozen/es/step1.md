# Cómo comprobar si un objeto está congelado profundamente

Para comprobar si un objeto está congelado profundamente, sigue los siguientes pasos en JavaScript:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza la recursividad para comprobar si todas las propiedades del objeto están congeladas profundamente.
3. Utiliza `Object.isFrozen()` en el objeto dado para comprobar si está congelado superficialmente.
4. Utiliza `Object.keys()` para obtener todas las propiedades del objeto y `Array.prototype.every()` para comprobar que todas las claves son objetos congelados profundamente o valores no objeto.

A continuación, se muestra un fragmento de código de ejemplo para comprobar si un objeto está congelado profundamente:

```js
const isDeepFrozen = (obj) =>
  Object.isFrozen(obj) &&
  Object.keys(obj).every(
    (prop) => typeof obj[prop] !== "object" || isDeepFrozen(obj[prop])
  );
```

Puedes utilizar la función `isDeepFrozen` para comprobar si un objeto está congelado profundamente de la siguiente manera:

```js
const x = Object.freeze({ a: 1 });
const y = Object.freeze({ b: { c: 2 } });
isDeepFrozen(x); // true
isDeepFrozen(y); // false
```
