# Verificando se uma Data está Entre Duas Datas

Para verificar se uma data está entre outras duas datas, use os operadores "maior que" (`>`) e "menor que" (`<`) em JavaScript. Aqui está um exemplo de função:

```js
const isBetweenDates = (dateStart, dateEnd, date) =>
  date > dateStart && date < dateEnd;
```

Para usar esta função, passe a data de início, a data de fim e a data a ser verificada. A função retornará `true` se a data estiver entre as datas de início e fim, e `false` caso contrário. Aqui estão alguns exemplos:

```js
isBetweenDates(
  new Date(2010, 11, 20),
  new Date(2010, 11, 30),
  new Date(2010, 11, 19)
); // false

isBetweenDates(
  new Date(2010, 11, 20),
  new Date(2010, 11, 30),
  new Date(2010, 11, 25)
); // true
```

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
