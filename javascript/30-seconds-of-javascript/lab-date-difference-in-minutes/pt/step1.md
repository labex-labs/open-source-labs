# Função para Calcular a Diferença de Data em Minutos

Para calcular a diferença (em minutos) entre duas datas, use a seguinte função:

```js
const getMinutesDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 60);
```

Simplesmente subtraia os dois objetos `Date` e divida pelo número de milissegundos em um minuto para obter a diferença (em minutos) entre eles.

Aqui está um exemplo de uso da função:

```js
getMinutesDiffBetweenDates(
  new Date("2021-04-24 01:00:15"),
  new Date("2021-04-24 02:00:15")
); // 60
```

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
