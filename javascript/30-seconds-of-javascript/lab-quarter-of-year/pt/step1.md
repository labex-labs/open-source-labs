# Função para Determinar o Trimestre do Ano

Para determinar o trimestre do ano, use a função `quarterOfYear()`. Esta função recebe um argumento opcional `date` e retorna um array com o trimestre e o ano a que a data fornecida pertence.

Para usar esta função, abra o Terminal/SSH e digite `node`. Em seguida, copie e cole o seguinte código:

```js
const quarterOfYear = (date = new Date()) => [
  Math.ceil((date.getMonth() + 1) / 3),
  date.getFullYear()
];
```

A função `quarterOfYear()` usa as seguintes etapas para calcular o trimestre e o ano:

- Usa `Date.prototype.getMonth()` para obter o mês atual no intervalo (0, 11), adiciona `1` para mapeá-lo para o intervalo (1, 12).
- Usa `Math.ceil()` e divide o mês por `3` para obter o trimestre atual.
- Usa `Date.prototype.getFullYear()` para obter o ano da `date` fornecida.
- Omite o argumento `date` para usar a data atual por padrão.

Aqui estão alguns exemplos de como usar a função `quarterOfYear()`:

```js
quarterOfYear(new Date("07/10/2018")); // [ 3, 2018 ]
quarterOfYear(); // [ 4, 2020 ]
```
