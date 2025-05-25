# Obtendo a Semana do Ano a partir de uma Data em JavaScript

Para obter a semana do ano indexada em zero que corresponde a uma data em JavaScript, siga estes passos:

1.  Crie uma função `weekOfYear` que recebe um parâmetro `date`.
2.  Use o construtor `Date` e `Date.prototype.getFullYear()` para obter o primeiro dia do ano como um objeto `Date`.
3.  Use `Date.prototype.setDate()`, `Date.prototype.getDate()` e `Date.prototype.getDay()` juntamente com o operador de módulo (`%`) para obter a primeira segunda-feira do ano.
4.  Subtraia a primeira segunda-feira do ano da `date` fornecida e divida pelo número de milissegundos em uma semana.
5.  Use `Math.round()` para obter a semana do ano indexada em zero correspondente à `date` fornecida.
6.  Se a `date` fornecida for anterior à primeira segunda-feira do ano, `-0` será retornado.

Aqui está o código:

```js
const weekOfYear = (date) => {
  const startOfYear = new Date(date.getFullYear(), 0, 1);
  startOfYear.setDate(startOfYear.getDate() + (startOfYear.getDay() % 7));
  return Math.round((date - startOfYear) / (7 * 24 * 3600 * 1000));
};
```

Para usar a função `weekOfYear`, basta chamá-la com um objeto `Date` como seu parâmetro:

```js
weekOfYear(new Date("2021-06-18")); // 23
```

Isso retornará a semana do ano indexada em zero que corresponde à data fornecida, que neste caso é `23`.
