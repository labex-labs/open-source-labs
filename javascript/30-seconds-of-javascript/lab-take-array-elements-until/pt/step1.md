# Removendo Elementos de um Array até que uma Condição seja Atendida

Para remover elementos em um array até que uma condição seja atendida e obter os elementos removidos, siga os passos abaixo:

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- Itere sobre o array usando um loop `for...of` sobre `Array.prototype.entries()` até que a função passada como argumento retorne um valor verdadeiro (truthy).
- Use `Array.prototype.slice()` para retornar os elementos removidos.
- A função de callback, `fn`, aceita um único argumento que é o valor do elemento.

Aqui está um exemplo de trecho de código:

```js
const takeUntil = (arr, fn) => {
  for (const [i, val] of arr.entries()) if (fn(val)) return arr.slice(0, i);
  return arr;
};

takeUntil([1, 2, 3, 4], (n) => n >= 3); // [1, 2]
```

No exemplo acima, a função `takeUntil()` é usada para remover elementos no array `[1, 2, 3, 4]` até que o valor seja maior ou igual a 3. A saída é `[1, 2]`.
