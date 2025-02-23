# Comprobando si un flujo es duplex

Para comprobar si un flujo es duplex (leíble y escribible), abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación. Luego, sigue estos pasos:

1. Comprueba si el argumento dado es diferente de `null`.
2. Utiliza `typeof` para comprobar si el argumento dado es de tipo `object` y si tiene una propiedad `pipe` de tipo `function`.
3. Además, comprueba si las propiedades `_read`, `_write`, `_readableState` y `_writableState` son de tipo `function` y `object`, respectivamente.

Aquí está el código:

```js
const isDuplexStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

Puedes probar este código utilizando el siguiente ejemplo:

```js
const Stream = require("stream");

isDuplexStream(new Stream.Duplex()); // true
```
