# Função para Retornar a Última Data de um Mês

Para começar a codificar, abra o Terminal/SSH e digite `node`.

Esta função retorna a última data do mês para a data fornecida.

Para conseguir isso, siga estes passos:

1.  Use `Date.prototype.getFullYear()` e `Date.prototype.getMonth()` para obter o ano e o mês atuais da data fornecida.
2.  Crie uma nova data com o ano e o mês fornecidos incrementados em `1`, e o dia definido como `0` (último dia do mês anterior). Você pode usar o construtor `Date` para este fim.
3.  Se nenhum argumento for passado para a função, ela usará a data atual por padrão.
4.  Retorne a última data do mês no formato de uma representação de string da data.

Aqui está o código para a função:

```js
const getLastDateOfMonth = (date = new Date()) => {
  let lastDate = new Date(date.getFullYear(), date.getMonth() + 1, 0);
  return lastDate.toISOString().split("T")[0];
};
```

Você pode testar a função chamando-a com um objeto de data assim:

```js
getLastDateOfMonth(new Date("2015-08-11")); // '2015-08-30'
```
