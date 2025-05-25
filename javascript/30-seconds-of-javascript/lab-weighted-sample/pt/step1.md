# Como Obter uma Amostra Ponderada de um Array em JavaScript

Para obter aleatoriamente um elemento de um array com base nos pesos fornecidos, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.reduce()` para criar um array de somas parciais para cada valor em `weights`.
3.  Use `Math.random()` para gerar um número aleatório e `Array.prototype.findIndex()` para encontrar o índice correto com base no array produzido anteriormente.
4.  Finalmente, retorne o elemento de `arr` com o índice produzido.

Aqui está o código para conseguir isso:

```js
const weightedSample = (arr, weights) => {
  let roll = Math.random();
  return arr[
    weights
      .reduce(
        (acc, w, i) => (i === 0 ? [w] : [...acc, acc[acc.length - 1] + w]),
        []
      )
      .findIndex((v, i, s) => roll >= (i === 0 ? 0 : s[i - 1]) && roll < v)
  ];
};
```

Você pode testar esta função passando um array e seus pesos correspondentes como argumentos:

```js
weightedSample([3, 7, 9, 11], [0.1, 0.2, 0.6, 0.1]); // 9
```
