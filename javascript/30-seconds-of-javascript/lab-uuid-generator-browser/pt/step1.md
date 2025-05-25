# Gerar UUID no Navegador

Para gerar um UUID compatível com [RFC4122](https://www.ietf.org/rfc/rfc4122.txt) versão 4 em um navegador, siga estes passos:

1. Abra o Terminal/SSH e digite `node`.
2. Use o método `Crypto.getRandomValues()` para gerar um UUID.
3. Converta o UUID em uma string hexadecimal usando o método `Number.prototype.toString()`.
4. Implemente o seguinte código:

```js
const UUIDGeneratorBrowser = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (
      c ^
      (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
    ).toString(16)
  );
```

5. Chame a função `UUIDGeneratorBrowser()` para gerar um UUID. Por exemplo, `UUIDGeneratorBrowser()` retornaria `'7982fcfe-5721-4632-bede-6000885be57d'`.
