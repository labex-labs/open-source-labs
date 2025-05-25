# Algoritmo de Particionamento de Array

Para particionar um array, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Aplique a função fornecida `fn` a cada valor no array `arr` fornecido.
3. Divida o array cada vez que `fn` retornar um novo valor.
4. Use `Array.prototype.reduce()` para criar um objeto acumulador que armazena o array resultante e o último valor retornado de `fn`.
5. Use `Array.prototype.push()` para adicionar cada valor em `arr` à partição apropriada no array acumulador.
6. Retorne o array resultante.

Aqui está a implementação do código:

```js
const partitionBy = (arr, fn) =>
  arr.reduce(
    ({ res, last }, v, i, a) => {
      const next = fn(v, i, a);
      if (next !== last) res.push([v]);
      else res[res.length - 1].push(v);
      return { res, last: next };
    },
    { res: [] }
  ).res;
```

Exemplo de uso:

```js
const numbers = [1, 1, 3, 3, 4, 5, 5, 5];
partitionBy(numbers, (n) => n % 2 === 0); // [[1, 1, 3, 3], [4], [5, 5, 5]]
partitionBy(numbers, (n) => n); // [[1, 1], [3, 3], [4], [5, 5, 5]]
```
