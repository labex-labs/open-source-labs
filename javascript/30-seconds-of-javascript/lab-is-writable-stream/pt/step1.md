# Verificando se um Fluxo é Gravável (Writable)

Para verificar se um fluxo é gravável, abra o Terminal/SSH e digite `node` para começar a praticar a codificação. Em seguida, siga estes passos:

1. Verifique se o argumento fornecido não é `null`.
2. Use `typeof` para verificar se o valor é um `object` e se a propriedade `pipe` é uma `function`.
3. Adicionalmente, verifique se o `typeof` das propriedades `_write` e `_writableState` são `function` e `object`, respectivamente.

Aqui está um exemplo de código que implementa essas verificações:

```js
const isWritableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

Você pode testar esta função usando o módulo `fs` em Node.js. Por exemplo:

```js
const fs = require("fs");

isWritableStream(fs.createWriteStream("test.txt")); // true
```
