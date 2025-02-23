# Así es como convertir un array en un objeto de identidad

Si quieres practicar la codificación, abre la Terminal/SSH y escribe `node`. Para convertir un array de valores en un objeto con los mismos valores como claves y valores, sigue estos pasos:

1. Utiliza `Array.prototype.map()` para mapear cada valor a un array de pares clave-valor.
2. Utiliza `Object.fromEntries()` para convertir el array de pares clave-valor en un objeto.

Aquí está el código:

```js
const toIdentityObject = (arr) => Object.fromEntries(arr.map((v) => [v, v]));
```

Y aquí está un ejemplo:

```js
toIdentityObject(["a", "b"]); // { a: 'a', b: 'b' }
```
