# Cómo simbolizar las claves de un objeto en JavaScript

Para simbolizar las claves de un objeto en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `Object.keys()` para obtener las claves del objeto que desea simbolizar.
3. Utilice el método `Array.prototype.reduce()` y `Symbol` para crear un nuevo objeto donde cada clave se convierte en un `Symbol`.
4. Aquí hay un fragmento de código de ejemplo:

```js
const symbolizeKeys = (obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({ ...acc, [Symbol(key)]: obj[key] }),
    {}
  );
```

5. Para probar la función, llame a `symbolizeKeys()` con su objeto como argumento, así:

```js
symbolizeKeys({ id: 10, name: "apple" });
// { [Symbol(id)]: 10, [Symbol(name)]: 'apple' }
```

Siguiendo estos pasos, puede simbolizar fácilmente las claves de cualquier objeto en JavaScript.
