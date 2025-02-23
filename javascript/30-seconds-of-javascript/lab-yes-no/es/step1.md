# Función para Comprobar Cadenas de Sí/No

Para comprobar si una cadena es una respuesta `'sí'` o `'no'`, utiliza la siguiente función en el Terminal/SSH escribiendo `node`:

```js
const yesNo = (val, def = false) =>
  /^(y|yes)$/i.test(val) ? true : /^(n|no)$/i.test(val) ? false : def;
```

- La función devuelve `true` si la cadena es `'y'`/`'yes'` y `false` si la cadena es `'n'`/`'no'`.
- Para establecer una respuesta predeterminada, omite el segundo argumento `def`. Por defecto, la función devolverá `false`.
- La función utiliza `RegExp.prototype.test()` para comprobar si la cadena coincide con `'y'`/`'yes'` o `'n'`/`'no'`.

Uso de ejemplo:

```js
yesNo("Y"); // true
yesNo("yes"); // true
yesNo("No"); // false
yesNo("Foo", true); // true
```
