# Comprobando si un flujo es escribible

Para comprobar si un flujo es escribible, abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación. Luego, siga estos pasos:

1. Compruebe si el argumento dado no es `null`.
2. Utilice `typeof` para comprobar si el valor es un `object` y si la propiedad `pipe` es una `function`.
3. Además, compruebe si el `typeof` de las propiedades `_write` y `_writableState` son `function` y `object`, respectivamente.

A continuación, se muestra un código de ejemplo que implementa estas comprobaciones:

```js
const isWritableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

Puede probar esta función utilizando el módulo `fs` en Node.js. Por ejemplo:

```js
const fs = require("fs");

isWritableStream(fs.createWriteStream("test.txt")); // true
```
