# Comprueba si un valor es un objeto plano

Para comprobar si un valor es un objeto plano, sigue estos pasos:

- Comprueba si el valor es verdadero.
- Utiliza `typeof` para comprobar si es un objeto.
- Utiliza `Object.prototype.constructor` para asegurarte de que el constructor sea igual a `Object`.

Utiliza el siguiente código para implementar esta comprobación:

```js
const isPlainObject = (val) =>
  !!val && typeof val === "object" && val.constructor === Object;
```

Puedes probar esta función con los siguientes ejemplos:

```js
isPlainObject({ a: 1 }); // true
isPlainObject(new Map()); // false
```

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.
