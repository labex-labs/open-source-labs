# Como Contar Ocorrências em JavaScript

Para contar o número de vezes que um valor específico ocorre em um array JavaScript, você pode usar o método `Array.prototype.reduce()`.

Veja como você pode fazer isso:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Copie e cole o seguinte código:

```js
const countOccurrences = (arr, val) =>
  arr.reduce((a, v) => (v === val ? a + 1 : a), 0);
```

3. No código acima, a função `countOccurrences` recebe dois argumentos: o array a ser pesquisado e o valor a ser contado.
4. O método `reduce()` é usado para iterar sobre cada elemento no array e incrementar um contador cada vez que o valor específico é encontrado.
5. Para testar a função, chame-a com um array e um valor, assim:

```js
countOccurrences([1, 1, 2, 1, 2, 3], 1); // 3
```

Isso retornará o número de vezes que `1` ocorre no array `[1, 1, 2, 1, 2, 3]`, que é `3`.
