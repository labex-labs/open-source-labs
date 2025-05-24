# Codificando uma String para Base64

Para codificar um objeto String para uma string ASCII codificada em base64, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a codificar.
2.  Crie um `Buffer` usando a string fornecida e a codificação binária.
3.  Use `Buffer.prototype.toString()` para retornar a string codificada em base64.

Aqui está um trecho de código de exemplo:

```js
const encodeToBase64 = (str) => Buffer.from(str, "binary").toString("base64");
```

Agora você pode usar a função `encodeToBase64()` para codificar qualquer string para base64. Por exemplo:

```js
encodeToBase64("foobar"); // 'Zm9vYmFy'
```
