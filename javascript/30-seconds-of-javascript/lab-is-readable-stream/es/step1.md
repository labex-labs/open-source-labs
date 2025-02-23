# Comprobar si un flujo es legible

Para comprobar si un argumento dado es un flujo legible, siga estos pasos:

- Primero, abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
- Compruebe si el valor no es `null`.
- Utilice `typeof` para comprobar si el valor es un `object` y la propiedad `pipe` es una `function`.
- Además, compruebe si el `typeof` de las propiedades `_read` y `_readableState` son `function` y `object`, respectivamente.

A continuación, se muestra una función de ejemplo que implementa estos pasos:

```js
const isReadableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object";
```

Puede usar esta función para comprobar si un flujo es legible, de la siguiente manera:

```js
const fs = require("fs");

isReadableStream(fs.createReadStream("test.txt")); // true
```
