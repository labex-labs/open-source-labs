# Função JavaScript para Encontrar o Último Valor Correspondente

Para encontrar o último elemento em um array que satisfaz uma determinada condição, use a seguinte função JavaScript:

```js
const findLast = (arr, fn) => arr.filter(fn).pop();
```

Para usar esta função, passe o array que você deseja pesquisar e uma função que retorna um valor truthy para os elementos que você deseja corresponder.

Por exemplo, `findLast([1, 2, 3, 4], n => n % 2 === 1);` retornará `3`, pois encontra o último número ímpar no array.

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
