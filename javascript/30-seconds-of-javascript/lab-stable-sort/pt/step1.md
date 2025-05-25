# Ordenação Estável (Stable Sort)

Para realizar a ordenação estável (stable sorting) de um array e preservar os índices iniciais dos itens com os mesmos valores, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `Array.prototype.map()` para emparelhar cada elemento do array de entrada com seu índice correspondente.
3. Use `Array.prototype.sort()` juntamente com uma função `compare` para ordenar a lista, preservando a ordem inicial se os itens comparados forem iguais.
4. Use `Array.prototype.map()` novamente para converter os itens do array de volta à sua forma inicial.
5. O array original não é mutado, e um novo array é retornado em vez disso.

Aqui está uma implementação da função `stableSort` em JavaScript:

```js
const stableSort = (arr, compare) =>
  arr
    .map((item, index) => ({ item, index }))
    .sort((a, b) => compare(a.item, b.item) || a.index - b.index)
    .map(({ item }) => item);
```

Você pode chamar a função `stableSort` com um array e uma função `compare` para obter um novo array com os itens ordenados, como mostrado abaixo:

```js
const arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const stable = stableSort(arr, () => 0); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
