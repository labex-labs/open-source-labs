# Instruções para Calcular a Média de um Array Mapeado

Para calcular a média de um array, você pode mapear cada elemento para um novo valor usando a função fornecida. Aqui estão os passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.map()` para mapear cada elemento para o valor retornado por `fn`.
3.  Use `Array.prototype.reduce()` para adicionar cada valor mapeado a um acumulador, inicializado com o valor `0`.
4.  Divida o array resultante pelo seu comprimento para obter a média.

Aqui está o código que você pode usar:

```js
const averageBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => acc + val, 0) / arr.length;
```

Você pode testar esta função usando os seguintes exemplos:

```js
averageBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (o) => o.n); // 5
averageBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 5
```
