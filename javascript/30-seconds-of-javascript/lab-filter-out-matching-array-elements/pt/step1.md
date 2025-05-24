# Como Filtrar Elementos Correspondentes de um Array em JavaScript

Para filtrar elementos em um array JavaScript que possuem um ou mais valores especificados, siga estas etapas:

1.  Abra o Terminal ou SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Array.prototype.includes()` para encontrar os valores a serem excluídos.
3.  Use o método `Array.prototype.filter()` para criar um novo array com os elementos excluídos.

Aqui está um exemplo de trecho de código:

```js
const without = (arr, ...args) => arr.filter((v) => !args.includes(v));

without([2, 1, 2, 3], 1, 2); // [3]
```

Neste exemplo, a função `without` recebe um array `arr` e um ou mais argumentos `args`. A função usa o método `filter()` para criar um novo array que exclui quaisquer elementos que correspondam a qualquer um dos valores especificados em `args`. O método `includes()` é usado para verificar se o valor está em `args`. Finalmente, a função retorna o novo array com os elementos excluídos.
