# Función para Comprobar si un Valor es de un Tipo Determinado

Para comprobar si un valor proporcionado es de un tipo especificado, siga estos pasos:

- Asegúrese de que el valor no sea `undefined` o `null` utilizando `Array.prototype.includes()`.
- Utilice `Object.prototype.constructor` para comparar la propiedad constructor del valor con el `type` especificado.
- La función `is()` que se muestra a continuación realiza estas comprobaciones y devuelve `true` si el valor es del tipo especificado, y `false` en caso contrario.

```js
const is = (type, val) => ![, null].includes(val) && val.constructor === type;
```

Puede utilizar `is()` para comprobar si un valor es de varios tipos, como `Array`, `ArrayBuffer`, `Map`, `RegExp`, `Set`, `WeakMap`, `WeakSet`, `String`, `Number` y `Boolean`. Por ejemplo:

```js
is(Array, [1]); // true
is(Map, new Map()); // true
is(String, ""); // true
is(Number, 1); // true
is(Boolean, true); // true
```
