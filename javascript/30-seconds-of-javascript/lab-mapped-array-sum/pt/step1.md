# Função para Calcular a Soma dos Elementos de um Array Mapeado

Para calcular a soma de um array mapeando cada elemento para um valor usando uma função fornecida, use a função `sumBy`. Esta função usa `Array.prototype.map()` para mapear cada elemento para o valor retornado por `fn`. Em seguida, usa `Array.prototype.reduce()` para adicionar cada valor a um acumulador, que é inicializado com o valor `0`.

```js
const sumBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => acc + val, 0);
```

Exemplo de Uso:

```js
sumBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // Retorna 20
sumBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // Retorna 20
```

Para começar a praticar a codificação com esta função, abra o Terminal/SSH e digite `node`.
