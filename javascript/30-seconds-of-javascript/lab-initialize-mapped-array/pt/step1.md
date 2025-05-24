# Inicializando um Array Mapeado em JavaScript

Para inicializar um array mapeado em JavaScript, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use o construtor `Array()` para criar um array com o comprimento desejado.
3. Use `Array.prototype.fill()` para preencher o array com valores `null`.
4. Use `Array.prototype.map()` para preencher o array com os valores desejados, usando a função fornecida, `mapFn`.
5. Omita o segundo argumento, `mapFn`, para mapear cada elemento para seu índice.

Aqui está um exemplo de trecho de código:

```js
const initializeMappedArray = (n, mapFn = (_, i) => i) =>
  Array(n).fill(null).map(mapFn);
```

Você pode usar a função `initializeMappedArray` para criar um array mapeado com os valores desejados:

```js
initializeMappedArray(5); // [0, 1, 2, 3, 4]
initializeMappedArray(5, (i) => `item ${i + 1}`);
// ['item 1', 'item 2', 'item 3', 'item 4', 'item 5']
```
