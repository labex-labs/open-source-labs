# Chunk Iterable (Iterável em Blocos)

Para dividir um iterável em _arrays_ menores de um tamanho especificado, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use um loop `for...of` sobre o iterável fornecido, usando `Array.prototype.push()` para adicionar cada novo valor ao `chunk` (bloco) atual.
3.  Verifique se o `chunk` atual tem o `size` (tamanho) desejado usando `Array.prototype.length` e use `yield` para retornar o valor, caso seja verdade.
4.  Verifique o `chunk` final usando `Array.prototype.length` e use `yield` para retorná-lo se não estiver vazio.
5.  Use o seguinte código:

```js
const chunkify = function* (itr, size) {
  let chunk = [];
  for (const v of itr) {
    chunk.push(v);
    if (chunk.length === size) {
      yield chunk;
      chunk = [];
    }
  }
  if (chunk.length) yield chunk;
};
```

6.  Use este código para testar a função:

```js
const x = new Set([1, 2, 1, 3, 4, 1, 2, 5]);
[...chunkify(x, 2)]; // [[1, 2], [3, 4], [5]]
```
