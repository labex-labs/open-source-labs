# Como Dividir um Array em N Pedaços

Para dividir um array em `n` arrays menores, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Math.ceil()` e `Array.prototype.length` para calcular o tamanho de cada pedaço (chunk).
3.  Use `Array.from()` para criar um novo array de tamanho `n`.
4.  Use `Array.prototype.slice()` para mapear cada elemento do novo array para um pedaço do tamanho de `size`.
5.  Se o array original não puder ser dividido uniformemente, o pedaço final conterá os elementos restantes.

Aqui está um exemplo de implementação da função `chunkIntoN` em JavaScript:

```js
const chunkIntoN = (arr, n) => {
  const size = Math.ceil(arr.length / n);
  return Array.from({ length: n }, (v, i) =>
    arr.slice(i * size, i * size + size)
  );
};
```

Você pode usar esta função para dividir um array em `n` pedaços, passando o array e o número desejado de pedaços como argumentos. Por exemplo:

```js
chunkIntoN([1, 2, 3, 4, 5, 6, 7], 4); // [[1, 2], [3, 4], [5, 6], [7]]
```
