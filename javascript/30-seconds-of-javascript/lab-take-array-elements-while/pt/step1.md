# Removendo Elementos de um Array com Base em uma Condição

Para remover elementos em um array com base em uma condição, abra o Terminal/SSH e digite `node`.

A função `takeWhile` remove elementos em um array até que a função passada retorne `false` e, em seguida, retorna os elementos removidos.

Aqui estão os passos para usar a função `takeWhile`:

- Itere sobre o array usando um loop `for...of` sobre `Array.prototype.entries()`.
- Itere até que o valor retornado da função seja falsy.
- Retorne os elementos removidos usando `Array.prototype.slice()`.
- A função de callback `fn` aceita um único argumento, que é o valor do elemento.

Use o seguinte código para implementar a função `takeWhile`:

```js
const takeWhile = (arr, fn) => {
  for (const [i, val] of arr.entries()) if (!fn(val)) return arr.slice(0, i);
  return arr;
};
```

Aqui está um exemplo de como usar a função `takeWhile` para remover elementos de um array com base em uma condição:

```js
takeWhile([1, 2, 3, 4], (n) => n < 3); // [1, 2]
```
