# Decodificando String Codificada em Base64

Para decodificar uma string de dados que foi codificada usando a codificação base-64, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Crie um `Buffer` para a string fornecida com codificação base-64.
3.  Use `Buffer.prototype.toString()` para retornar a string decodificada.

Aqui está um trecho de código de exemplo:

```js
const atob = (str) => Buffer.from(str, "base64").toString("binary");
```

Você pode testar esta função executando `atob('Zm9vYmFy')`, que deve retornar `'foobar'`.
