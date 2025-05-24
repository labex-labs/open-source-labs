# Classificação de Arrays

Para praticar a codificação, abra o Terminal/SSH e digite `node`. Esta função calcula a classificação de um array com base em uma função comparadora.

Para usar esta função, você pode:

- Usar `Array.prototype.map()` e `Array.prototype.filter()` para mapear cada elemento para uma classificação usando a função comparadora fornecida.

Aqui está um exemplo de uso:

```js
const ranking = (arr, compFn) =>
  arr.map((a) => arr.filter((b) => compFn(a, b)).length + 1);
```

Exemplo:

```js
ranking([8, 6, 9, 5], (a, b) => a < b);
// [2, 3, 1, 4]
ranking(["c", "a", "b", "d"], (a, b) => a.localeCompare(b) > 0);
// [3, 1, 2, 4]
```
