# Função para Calcular a Diferença de Data em Dias

Para calcular a diferença entre duas datas em dias, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use a função `getDaysDiffBetweenDates` com dois objetos `Date` como argumentos.
3. A função subtrairá a data inicial da data final e dividirá o resultado pelo número de milissegundos em um dia para obter a diferença em dias entre elas.

Aqui está o código para a função `getDaysDiffBetweenDates`:

```js
const getDaysDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600 * 24);
```

Para usar a função, passe dois objetos `Date` no formato `YYYY-MM-DD`:

```js
getDaysDiffBetweenDates(new Date("2017-12-13"), new Date("2017-12-22")); // 9
```

Isso retornará a diferença entre as duas datas em dias, que é 9 neste exemplo.
