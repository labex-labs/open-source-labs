# Explicação do Iterador "Flat"

Para criar um gerador que itera sobre um iterável e achata iteráveis aninhados, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use recursão na função geradora.
3.  Use um loop `for...of` para iterar sobre os valores do iterável fornecido.
4.  Use `Symbol.iterator` para verificar se cada valor é um iterável.
5.  Se for, use a expressão `yield*` para delegar recursivamente à mesma função geradora.
6.  Caso contrário, `yield` o valor atual.

Aqui está um trecho de código de exemplo:

```js
const flatIterator = function* (itr) {
  for (let item of itr) {
    if (item[Symbol.iterator]) yield* flatIterator(item);
    else yield item;
  }
};

const arr = [1, 2, [3, 4], [5, [6, [7], 8]], 9, new Set([10, 11])];
[...flatIterator(arr)]; // 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
```

No exemplo, `arr` é um array de valores, incluindo arrays aninhados e um conjunto (set). A função geradora `flatIterator` é usada para achatar esses valores aninhados e retornar um array achatado.
