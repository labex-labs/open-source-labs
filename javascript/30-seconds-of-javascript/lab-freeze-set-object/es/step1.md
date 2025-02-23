# Crear un objeto Set congelado en JavaScript

Para crear un objeto `Set` congelado en JavaScript, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza el constructor `Set` para crear un nuevo objeto `Set` a partir de un `iterable`.
3. Establece los métodos `add`, `delete` y `clear` del objeto recién creado en `undefined` para congelar efectivamente el objeto.

Aquí hay un fragmento de código de ejemplo:

```js
const frozenSet = (iterable) => {
  const s = new Set(iterable);
  s.add = undefined;
  s.delete = undefined;
  s.clear = undefined;
  return s;
};

console.log(frozenSet([1, 2, 3, 1, 2]));
// Output: Set { 1, 2, 3, add: undefined, delete: undefined, clear: undefined }
```

Este código crea un objeto `Set` congelado a partir de un iterable de números y devuelve el objeto con sus métodos `add`, `delete` y `clear` establecidos en `undefined`.
