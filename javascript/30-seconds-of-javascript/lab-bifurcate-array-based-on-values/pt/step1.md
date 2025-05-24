# Função para Dividir um Array em Dois Grupos

Para usar esta função para dividir um array em dois grupos com base nos valores, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use a função `bifurcate()`, que divide os valores em dois grupos com base no resultado do array `filter` fornecido.
3.  Para implementar a função, use `Array.prototype.reduce()` e `Array.prototype.push()` para adicionar elementos aos grupos, com base no array `filter`.
4.  Se `filter` tiver um valor truthy para qualquer elemento, adicione-o ao primeiro grupo; caso contrário, adicione-o ao segundo grupo.

Aqui está o código para a função `bifurcate()`:

```js
const bifurcate = (arr, filter) =>
  arr.reduce(
    (acc, val, i) => (acc[filter[i] ? 0 : 1].push(val), acc),
    [[], []]
  );
```

Você pode chamar a função `bifurcate()` com um array de valores e um array de filtro correspondente para dividir os valores em dois grupos. Por exemplo:

```js
bifurcate(["beep", "boop", "foo", "bar"], [true, true, false, true]);
// [ ['beep', 'boop', 'bar'], ['foo'] ]
```
