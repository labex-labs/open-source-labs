# Função para Adicionar Dias a uma Data

Aqui está uma função que pode calcular a data de `n` dias a partir da data fornecida e retornar sua representação em string.

Para usar a função, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o construtor `Date` para criar um objeto `Date` a partir do primeiro argumento.
3.  Use `Date.prototype.getDate()` e `Date.prototype.setDate()` para adicionar `n` dias à data fornecida.
4.  Use `Date.prototype.toISOString()` para retornar uma string no formato `yyyy-mm-dd`.

Aqui está o código da função:

```js
const addDaysToDate = (date, n) => {
  const d = new Date(date);
  d.setDate(d.getDate() + n);
  return d.toISOString().split("T")[0];
};
```

Você pode testar a função usando os seguintes exemplos:

```js
addDaysToDate("2020-10-15", 10); // '2020-10-25'
addDaysToDate("2020-10-15", -10); // '2020-10-05'
```
