# Como verificar se um valor é um Stream em Node.js

Para verificar se um valor é um stream em Node.js, você pode usar a função `isStream`. Para usar esta função, siga estes passos:

1. Abra o Terminal/SSH.
2. Digite `node` para começar a praticar a codificação.
3. Use a função `isStream` para verificar se o argumento fornecido é um stream.
4. Para verificar se o valor é diferente de `null`, use o seguinte código:

```js
const isStream = (val) =>
  val !== null && typeof val === "object" && typeof val.pipe === "function";
```

5. Para verificar se um arquivo é um stream, use o seguinte código:

```js
const fs = require("fs");

isStream(fs.createReadStream("test.txt")); // true
```
