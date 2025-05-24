# Remoção de Elementos de Array Baseada em Função

Para remover elementos específicos de um array, use a função `dropWhile`, que remove elementos até que a função passada retorne `true`. A função então retorna os elementos restantes no array.

Veja como funciona:

- Itera pelo array usando `Array.prototype.slice()` para remover o primeiro elemento do array até que o valor retornado de `func` seja `true`.
- Retorna os elementos restantes.

Exemplo de uso:

```js
const dropWhile = (arr, func) => {
  while (arr.length > 0 && !func(arr[0])) arr = arr.slice(1);
  return arr;
};

dropWhile([1, 2, 3, 4], (n) => n >= 3); // [3, 4]
```

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
