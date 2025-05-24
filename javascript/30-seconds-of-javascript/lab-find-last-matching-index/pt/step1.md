# Como Encontrar o Índice do Último Elemento Correspondente em um Array Usando JavaScript

Para encontrar o índice do último elemento que corresponde a uma determinada condição em um array JavaScript, use a função `findLastIndex`. Veja como usá-la:

```js
const findLastIndex = (arr, fn) =>
  (arr
    .map((val, i) => [i, val])
    .filter(([i, val]) => fn(val, i, arr))
    .pop() || [-1])[0];
```

A função `findLastIndex` recebe dois argumentos: o array a ser pesquisado e uma função para testar cada elemento. Veja como ela funciona:

1.  Use `Array.prototype.map()` para criar um novo array de pares `[índice, valor]`.
2.  Use `Array.prototype.filter()` para remover elementos do array que não correspondem à condição fornecida pela função `fn`.
3.  Use `Array.prototype.pop()` para obter o último elemento no array filtrado.
4.  Se o array filtrado estiver vazio, retorne `-1`.

Aqui está um exemplo de como usar `findLastIndex`:

```js
findLastIndex([1, 2, 3, 4], (n) => n % 2 === 1); // 2 (index of the value 3)
findLastIndex([1, 2, 3, 4], (n) => n === 5); // -1 (default value when not found)
```

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
