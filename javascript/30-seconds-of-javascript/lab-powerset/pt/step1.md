# Como Gerar o Powerset em JavaScript

Para gerar um powerset (conjunto das partes) de um array de números fornecido em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Array.prototype.reduce()` combinado com o método `Array.prototype.map()` para iterar sobre os elementos e combiná-los em um array contendo todas as combinações.
3.  Implemente o seguinte código:

```js
const powerset = (arr) =>
  arr.reduce((a, v) => a.concat(a.map((r) => r.concat(v))), [[]]);
```

4.  Para gerar o powerset, chame a função `powerset()` e passe o array como um argumento. Por exemplo:

```js
powerset([1, 2]); // [[], [1], [2], [1, 2]]
```

Isso retornará um array contendo todos os subconjuntos possíveis do array fornecido.
