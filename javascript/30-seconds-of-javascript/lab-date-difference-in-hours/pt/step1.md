# Função JavaScript para Calcular a Diferença de Data em Horas

Para calcular a diferença entre duas datas em horas usando JavaScript, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

2. Use a seguinte função JavaScript para obter a diferença (em horas) entre dois objetos `Date`:

```js
const getHoursDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600);
```

3. Chame a função com as duas datas como argumentos para obter a diferença em horas:

```js
getHoursDiffBetweenDates(
  new Date("2021-04-24 10:25:00"),
  new Date("2021-04-25 10:25:00")
); // 24
```
