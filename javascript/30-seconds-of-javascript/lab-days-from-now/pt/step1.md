# Função para Calcular a Data de 'n' Dias a Partir de Hoje

Para calcular a data 'n' dias a partir de hoje, siga estes passos:

- Abra o Terminal/SSH e digite 'node' para começar a praticar a codificação.
- Use o construtor `Date` para obter a data atual.
- Use `Math.abs()` e `Date.prototype.getDate()` para atualizar a data de acordo.
- Defina o resultado usando `Date.prototype.setDate()`.
- Use `Date.prototype.toISOString()` para retornar uma string no formato `yyyy-mm-dd`.

Aqui está o código:

```js
const daysFromNow = (n) => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + Math.abs(n));
  return currentDate.toISOString().split("T")[0];
};
```

Exemplo de uso:

```js
daysFromNow(5); // Output: 2020-10-13 (if current date is 2020-10-08)
```
