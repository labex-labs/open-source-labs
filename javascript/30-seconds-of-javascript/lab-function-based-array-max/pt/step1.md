# Como Encontrar o Valor Máximo de um Array com Base em uma Função

Para encontrar o valor máximo de um array com base em uma função, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.map()` para mapear cada elemento do array para o valor retornado pela função fornecida, `fn`.
3.  Use `Math.max()` para obter o valor máximo do array mapeado.

Aqui está um trecho de código de exemplo que implementa os passos acima:

```js
const maxBy = (arr, fn) =>
  Math.max(...arr.map(typeof fn === "function" ? fn : (val) => val[fn]));
```

Para usar a função `maxBy`, passe um array e a função que deve ser usada para mapear cada elemento para um valor. Você pode passar uma função diretamente ou uma string representando a chave que deve ser usada para acessar o valor em cada objeto do array.

Aqui estão alguns exemplos de chamadas para a função `maxBy`:

```js
maxBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // retorna 8
maxBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // retorna 8
```
