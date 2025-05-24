# Contar Dias Úteis Entre Duas Datas

Para contar os dias úteis entre duas datas, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.from()` para criar um array com um comprimento igual ao número de dias entre `startDate` e `endDate`.
3.  Use `Array.prototype.reduce()` para iterar sobre o array, verificando se cada data é um dia útil e incrementando `count`.
4.  Atualize `startDate` com o dia seguinte em cada loop usando `Date.prototype.getDate()` e `Date.prototype.setDate()` para avançá-lo em um dia.
5.  Observe que esta função não leva em consideração feriados oficiais.

Aqui está o código para implementar isso:

```js
const countWeekDaysBetween = (startDate, endDate) =>
  Array.from({ length: (endDate - startDate) / (1000 * 3600 * 24) }).reduce(
    (count) => {
      if (startDate.getDay() % 6 !== 0) count++;
      startDate = new Date(startDate.setDate(startDate.getDate() + 1));
      return count;
    },
    0
  );
```

Você pode usar o seguinte código para testar a função:

```js
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 06, 2020")); // 1
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 14, 2020")); // 7
```
