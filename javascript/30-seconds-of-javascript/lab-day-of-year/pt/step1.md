# Como Obter o Dia do Ano em JavaScript usando o Objeto Date

Para obter o dia do ano (número entre 1-366) de um objeto `Date` em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o construtor `Date` e `Date.prototype.getFullYear()` para obter o primeiro dia do ano como um objeto `Date`.
3.  Subtraia o primeiro dia do ano do objeto `date` e divida pelos milissegundos em cada dia para obter o resultado.
4.  Use `Math.floor()` para arredondar a contagem de dias resultante para um inteiro.

Aqui está o código:

```js
const dayOfYear = (date) =>
  Math.floor((date - new Date(date.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24);
```

Para testar a função, chame `dayOfYear()` com um objeto `Date` como argumento:

```js
dayOfYear(new Date()); // 272
```
