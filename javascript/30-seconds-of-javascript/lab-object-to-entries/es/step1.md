# Convertir un objeto en una matriz de pares clave-valor

Para convertir un objeto en una matriz de pares clave-valor, utiliza el método `Object.keys()` y el método `Array.prototype.map()`. Esto iterará sobre las claves del objeto y producirá una matriz con pares clave-valor. Alternativamente, puedes usar el método `Object.entries()`, que proporciona una funcionalidad similar.

A continuación, se muestra un fragmento de código de ejemplo que muestra cómo convertir un objeto en una matriz de pares clave-valor:

```js
const objectToEntries = (obj) => Object.keys(obj).map((k) => [k, obj[k]]);
```

Puedes usar la función `objectToEntries()` para convertir un objeto en una matriz de pares clave-valor de la siguiente manera:

```js
objectToEntries({ a: 1, b: 2 }); // [ ['a', 1], ['b', 2] ]
```
