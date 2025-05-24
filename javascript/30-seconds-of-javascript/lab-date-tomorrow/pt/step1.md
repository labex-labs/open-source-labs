# Obtendo a Data de Amanhã

Para praticar a codificação, você pode começar abrindo o Terminal/SSH e digitando `node`. Depois de fazer isso, você pode obter a data de amanhã com os seguintes passos:

1.  Use o construtor `Date` para obter a data atual.
2.  Incremente-a em um usando `Date.prototype.getDate()`.
3.  Defina o valor para o resultado usando `Date.prototype.setDate()`.
4.  Use `Date.prototype.toISOString()` para retornar uma string no formato `yyyy-mm-dd`.

Aqui está o código que você pode usar:

```js
const tomorrow = () => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + 1);
  return currentDate.toISOString().split("T")[0];
};
```

Depois de inserir este código, você pode obter a data de amanhã chamando a função `tomorrow()`. Por exemplo, se a data de hoje for 2018-10-18, a saída será `2018-10-19`.
