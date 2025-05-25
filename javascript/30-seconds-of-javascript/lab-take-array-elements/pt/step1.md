# Como remover elementos de um array em JavaScript

Para remover elementos do início de um array em JavaScript, siga estes passos:

1.  Abra o Terminal ou SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Array.prototype.slice()` para criar um novo array com `n` elementos removidos do início.
3.  Use a função `take` no trecho de código abaixo para implementar a lógica.

```js
const take = (arr, n = 1) => arr.slice(0, n);
```

Aqui está um exemplo de como usar a função `take`:

```js
take([1, 2, 3], 5); // [1, 2, 3]
take([1, 2, 3], 0); // []
```

No primeiro exemplo, `take([1, 2, 3], 5)` retorna `[1, 2, 3]` porque há apenas 3 elementos no array. No segundo exemplo, `take([1, 2, 3], 0)` retorna `[]` porque nenhum elemento é retirado do início do array.
