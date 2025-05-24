# Função JavaScript para Calcular Dias Atrás

Aqui está uma função JavaScript que calcula a data de `n` dias atrás a partir de hoje e a retorna como uma string no formato `yyyy-mm-dd`:

```js
const daysAgo = (n) => {
  const today = new Date();
  const daysAgoDate = new Date(today.setDate(today.getDate() - Math.abs(n)));
  return daysAgoDate.toISOString().split("T")[0];
};
```

Como funciona:

- O construtor `Date` é usado para obter a data atual.
- A função `Math.abs()` é usada para garantir que o número de dias seja positivo.
- A função `Date.prototype.getDate()` é usada para obter o dia do mês para a data atual.
- A função `Date.prototype.setDate()` é usada para atualizar a data de acordo.
- A data resultante é retornada como uma string no formato `yyyy-mm-dd` usando a função `Date.prototype.toISOString()`.

Exemplo de uso:

```js
daysAgo(20); // "2020-09-16" (se a data atual for 2020-10-06)
```
