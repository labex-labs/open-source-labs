# Cómo comprobar si un valor es un flujo en Node.js

Para comprobar si un valor es un flujo en Node.js, puedes usar la función `isStream`. Para usar esta función, sigue estos pasos:

1. Abre la Terminal/SSH.
2. Escribe `node` para comenzar a practicar la codificación.
3. Utiliza la función `isStream` para comprobar si el argumento dado es un flujo.
4. Para comprobar si el valor es diferente de `null`, utiliza el siguiente código:

```js
const isStream = (val) =>
  val !== null && typeof val === "object" && typeof val.pipe === "function";
```

5. Para comprobar si un archivo es un flujo, utiliza el siguiente código:

```js
const fs = require("fs");

isStream(fs.createReadStream("test.txt")); // true
```
