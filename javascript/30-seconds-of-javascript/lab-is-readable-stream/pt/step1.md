# Verificar se um Stream é Legível

Para verificar se um determinado argumento é um stream legível, siga estes passos:

- Primeiro, abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- Verifique se o valor não é `null`.
- Use `typeof` para verificar se o valor é um `object` e se a propriedade `pipe` é uma `function`.
- Adicionalmente, verifique se o `typeof` das propriedades `_read` e `_readableState` são `function` e `object`, respectivamente.

Aqui está um exemplo de função que implementa esses passos:

```js
const isReadableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object";
```

Você pode usar esta função para verificar se um stream é legível, assim:

```js
const fs = require("fs");

isReadableStream(fs.createReadStream("test.txt")); // true
```
