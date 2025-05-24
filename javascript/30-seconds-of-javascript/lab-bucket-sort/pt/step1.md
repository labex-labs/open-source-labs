# Algoritmo de Ordenação por Baldes (Bucket Sort)

Para usar o algoritmo de ordenação por baldes e ordenar um array de números, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Encontre os valores mínimo e máximo do array fornecido usando `Math.min()`, `Math.max()` e o operador spread (`...`).
3.  Crie o número apropriado de `baldes` (arrays vazios) usando `Array.from()` e `Math.floor()`.
4.  Preencha cada balde com os elementos apropriados do array usando `Array.prototype.forEach()`.
5.  Ordene cada balde e adicione-o ao resultado usando `Array.prototype.reduce()`, o operador spread (`...`) e `Array.prototype.sort()`.

Aqui está um exemplo de implementação do algoritmo de ordenação por baldes em JavaScript:

```js
const bucketSort = (arr, size = 5) => {
  const min = Math.min(...arr);
  const max = Math.max(...arr);
  const buckets = Array.from(
    { length: Math.floor((max - min) / size) + 1 },
    () => []
  );
  arr.forEach((val) => {
    buckets[Math.floor((val - min) / size)].push(val);
  });
  return buckets.reduce((acc, b) => [...acc, ...b.sort((a, b) => a - b)], []);
};
```

Para testar o algoritmo, execute o seguinte código:

```js
bucketSort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
