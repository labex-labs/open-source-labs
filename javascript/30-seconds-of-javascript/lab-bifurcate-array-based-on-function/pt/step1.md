# Função para Dividir um Array em Dois Grupos

Para dividir um array em dois grupos com base no resultado de uma função fornecida, siga estas etapas:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use os métodos `Array.prototype.reduce()` e `Array.prototype.push()` para adicionar elementos aos grupos. Isso é baseado no valor retornado pela função fornecida `fn` para cada elemento.
3.  Se `fn` retornar um valor verdadeiro (truthy) para qualquer elemento, adicione-o ao primeiro grupo. Caso contrário, adicione-o ao segundo grupo.

Aqui está o código:

```js
const bifurcateBy = (arr, fn) =>
  arr.reduce(
    (acc, val, i) => (acc[fn(val, i) ? 0 : 1].push(val), acc),
    [[], []]
  );
```

Por exemplo, se você chamar `bifurcateBy(['beep', 'boop', 'foo', 'bar'], x => x[0] === 'b')`, a função retornará `[ ['beep', 'boop', 'bar'], ['foo'] ]`.
