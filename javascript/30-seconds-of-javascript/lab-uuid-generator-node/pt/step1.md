# Gerando UUID no Node.js

Para gerar um UUID no Node.js, siga os passos abaixo:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `crypto.randomBytes()` para gerar um UUID que esteja em conformidade com a versão 4 do [RFC4122](https://www.ietf.org/rfc/rfc4122.txt).
3.  Converta o UUID gerado em um UUID adequado (string hexadecimal) usando o método `Number.prototype.toString()`.
4.  Alternativamente, você pode usar o método [`crypto.randomUUID()`](https://nodejs.org/api/crypto.html#cryptorandomuuidoptions) que fornece funcionalidade semelhante.

Aqui está um trecho de código de exemplo para gerar um UUID no Node.js:

```js
const crypto = require("crypto");

const UUIDGeneratorNode = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (c ^ (crypto.randomBytes(1)[0] & (15 >> (c / 4)))).toString(16)
  );
```

Você pode chamar o método `UUIDGeneratorNode()` para gerar um UUID.

```js
UUIDGeneratorNode(); // '79c7c136-60ee-40a2-beb2-856f1feabefc'
```
