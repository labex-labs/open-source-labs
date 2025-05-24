# Função para Adicionar Minutos à Data

Para adicionar um número específico de minutos a uma data fornecida, use a seguinte função:

```js
const addMinutesToDate = (date, n) => {
  // Create a Date object from the given date
  const d = new Date(date);
  // Add n minutes to the Date object
  d.setTime(d.getTime() + n * 60000);
  // Return a string representation of the new date in yyyy-mm-dd HH:MM:SS format
  return d.toISOString().split(".")[0].replace("T", " ");
};
```

Para usar esta função, passe uma representação de string da data como o primeiro argumento e o número de minutos a adicionar (ou subtrair, se negativo) como o segundo argumento. Por exemplo:

```js
addMinutesToDate("2020-10-19 12:00:00", 10); // '2020-10-19 12:10:00'
addMinutesToDate("2020-10-19", -10); // '2020-10-18 23:50:00'
```

Observe que a função retorna a nova data como uma string no formato `yyyy-mm-dd HH:MM:SS`.
