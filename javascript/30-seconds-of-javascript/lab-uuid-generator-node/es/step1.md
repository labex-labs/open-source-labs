# Generando UUID en Node.js

Para generar un UUID en Node.js, siga los pasos siguientes:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `crypto.randomBytes()` para generar un UUID que sea compatible con la versión 4 de [RFC4122](https://www.ietf.org/rfc/rfc4122.txt).
3. Convierta el UUID generado en un UUID adecuado (cadena hexadecimal) utilizando el método `Number.prototype.toString()`.
4. Alternativamente, puede utilizar el método [`crypto.randomUUID()`](https://nodejs.org/api/crypto.html#cryptorandomuuidoptions) que proporciona una funcionalidad similar.

A continuación, se muestra un fragmento de código de ejemplo para generar un UUID en Node.js:

```js
const crypto = require("crypto");

const UUIDGeneratorNode = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (c ^ (crypto.randomBytes(1)[0] & (15 >> (c / 4)))).toString(16)
  );
```

Puede llamar al método `UUIDGeneratorNode()` para generar un UUID.

```js
UUIDGeneratorNode(); // '79c7c136-60ee-40a2-beb2-856f1feabefc'
```
