# Função para Retornar o Valor Mínimo de um Array

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Esta função retorna o valor mínimo de um array, com base na função fornecida.

Para fazer isso, ela usa `Array.prototype.map()` para mapear cada elemento para o valor retornado pela função. Em seguida, usa `Math.min()` para obter o valor mínimo.

```js
const minBy = (arr, fn) =>
  Math.min(...arr.map(typeof fn === "function" ? fn : (val) => val[fn]));
```

Você pode usar esta função passando um array e uma função. Por exemplo:

```js
minBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // 2
minBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 2
```
