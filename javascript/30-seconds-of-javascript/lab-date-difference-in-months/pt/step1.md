# Função para Calcular a Diferença de Datas em Meses

Para calcular a diferença entre duas datas em meses, use a seguinte função:

```js
const getMonthsDiffBetweenDates = (dateInitial, dateFinal) =>
  Math.max(
    (dateFinal.getFullYear() - dateInitial.getFullYear()) * 12 +
      dateFinal.getMonth() -
      dateInitial.getMonth(),
    0
  );
```

Para usar esta função, passe dois objetos `Date` como argumentos. Por exemplo:

```js
getMonthsDiffBetweenDates(new Date("2017-12-13"), new Date("2018-04-29")); // 4
```

Esta função usa os métodos `Date.prototype.getFullYear()` e `Date.prototype.getMonth()` para calcular a diferença em meses entre duas datas.
