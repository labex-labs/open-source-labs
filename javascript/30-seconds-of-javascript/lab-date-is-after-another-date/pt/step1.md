# Como Verificar se uma Data é Posterior a Outra em JavaScript

Para verificar se uma data vem depois de outra em JavaScript, você pode usar o operador maior que (`>`). Aqui está um trecho de código de exemplo que verifica se uma determinada data (`dateA`) é posterior a outra data (`dateB`):

```js
const isAfterDate = (dateA, dateB) => dateA > dateB;
```

Para usar esta função, basta passar dois objetos de data, assim:

```js
isAfterDate(new Date(2010, 10, 21), new Date(2010, 10, 20)); // true
```

Para experimentar isso, você pode abrir o Terminal/SSH e digitar `node` para começar a praticar a codificação.
