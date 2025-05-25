# Código para Verificar Ano Bissexto

Para verificar se um determinado `ano` é um ano bissexto, siga estes passos:

1.  Abra o Terminal/SSH.
2.  Digite `node` para começar a codificar.
3.  Use o construtor `Date` e defina a data para 29 de fevereiro do `ano` fornecido.
4.  Verifique se o mês é igual a `1` usando `Date.prototype.getMonth()`.
5.  Use o seguinte trecho de código para verificar se um ano é bissexto:

```js
const isLeapYear = (year) => new Date(year, 1, 29).getMonth() === 1;
```

Aqui está um exemplo de como usar este código:

```js
isLeapYear(2019); // false
isLeapYear(2020); // true
```
