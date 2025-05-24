# Como Criar um Objeto Date a partir de um Timestamp Unix

Para criar um objeto `Date` a partir de um timestamp Unix, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Multiplique o timestamp por `1000` para convertê-lo em milissegundos.
3.  Use o construtor `Date` para criar um novo objeto `Date`.

Aqui está um trecho de código de exemplo:

```js
const fromTimestamp = (timestamp) => new Date(timestamp * 1000);
```

Você pode usar esta função para converter um timestamp Unix em um objeto `Date` assim:

```js
fromTimestamp(1602162242); // 2020-10-08T13:04:02.000Z
```
