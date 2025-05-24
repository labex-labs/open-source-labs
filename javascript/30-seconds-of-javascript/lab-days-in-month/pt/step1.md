# Função JavaScript para Obter o Número de Dias em um Mês

Para encontrar o número de dias em um mês específico de um determinado ano usando JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Crie uma função chamada `diasNoMes` (daysInMonth) que recebe dois parâmetros: `ano` (year) e `mês` (month).
3.  Dentro da função `diasNoMes`, use o construtor `Date` para criar um objeto de data a partir do `ano` e `mês` fornecidos.
4.  Defina o parâmetro de dias como `0` para obter o último dia do mês anterior, já que os meses são indexados a partir de zero.
5.  Use `Date.prototype.getDate()` para retornar o número de dias no `mês` fornecido.
6.  Retorne o número de dias da função `diasNoMes`.

Aqui está o código JavaScript para a função `diasNoMes`:

```js
const daysInMonth = (year, month) => new Date(year, month, 0).getDate();
```

Você pode usar a função `diasNoMes` para obter o número de dias em qualquer mês de qualquer ano, como mostrado nestes exemplos:

```js
daysInMonth(2020, 12); // 31
daysInMonth(2024, 2); // 29
```
