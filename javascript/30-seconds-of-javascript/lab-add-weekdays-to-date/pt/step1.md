# Função para Adicionar Dias Úteis a uma Data Dada

Para calcular uma data futura adicionando um determinado número de dias úteis, você pode usar a função `addWeekDays`. Aqui estão os passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use a função `addWeekDays` que recebe dois argumentos: `startDate` e `count`.
3.  `startDate` é a data a partir da qual você deseja começar a adicionar dias úteis.
4.  `count` é o número de dias úteis que você deseja adicionar à data de início.
5.  A função constrói um array usando o método `Array.from()` e define o comprimento igual ao `count` de dias úteis a serem adicionados.
6.  O método `Array.prototype.reduce()` é usado para iterar sobre o array, começando de `startDate` e incrementando-o usando `Date.prototype.getDate()` e `Date.prototype.setDate()`.
7.  A função verifica se a `date` atual é em um fim de semana ou não.
8.  Se a `date` atual for em um fim de semana, a função a atualiza novamente adicionando um ou dois dias para torná-la um dia útil.
9.  A função não leva em consideração feriados oficiais.

```js
const addWeekDays = (startDate, count) =>
  Array.from({ length: count }).reduce((date) => {
    date = new Date(date.setDate(date.getDate() + 1));
    if (date.getDay() % 6 === 0)
      date = new Date(date.setDate(date.getDate() + (date.getDay() / 6 + 1)));
    return date;
  }, startDate);
```

Aqui estão alguns exemplos de como você pode usar a função `addWeekDays`:

```js
addWeekDays(new Date("Oct 09, 2020"), 5); // 'Oct 16, 2020'
addWeekDays(new Date("Oct 12, 2020"), 5); // 'Oct 19, 2020'
```
