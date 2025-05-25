# Verificando se um Stream é Duplex

Para verificar se um stream é duplex (legível e gravável), abra o Terminal/SSH e digite `node` para começar a praticar a codificação. Em seguida, siga estas etapas:

1.  Verifique se o argumento fornecido é diferente de `null`.
2.  Use `typeof` para verificar se o argumento fornecido é do tipo `object` e se possui uma propriedade `pipe` do tipo `function`.
3.  Adicionalmente, verifique se as propriedades `_read`, `_write`, `_readableState` e `_writableState` são do tipo `function` e `object`, respectivamente.

Aqui está o código:

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

Você pode testar este código usando o seguinte exemplo:

```js
const Stream = require("stream");

isDuplexStream(new Stream.Duplex()); // true
```
