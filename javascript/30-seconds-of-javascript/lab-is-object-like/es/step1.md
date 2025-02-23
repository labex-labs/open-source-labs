# Comprobando si un valor es similar a un objeto

Para comprobar si un valor es similar a un objeto, siga estos pasos:

1. Abra la Terminal/SSH.
2. Escriba `node` para comenzar a practicar la codificación.
3. Compruebe si el valor proporcionado no es `null` y su `typeof` es igual a `'object'`.

Aquí está el código que puede utilizar:

```js
const isObjectLike = (val) => val !== null && typeof val === "object";
```

Puede probar esta función con los siguientes ejemplos:

```js
isObjectLike({}); // true
isObjectLike([1, 2, 3]); // true
isObjectLike((x) => x); // false
isObjectLike(null); // false
```
