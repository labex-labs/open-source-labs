# Encontrando Arrays de Elementos Consecutivos

Para encontrar arrays de elementos consecutivos, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.slice()` para criar um array com `n - 1` elementos removidos do início.
3.  Use `Array.prototype.map()` e `Array.prototype.slice()` para mapear cada elemento para um array de `n` elementos consecutivos.

Aqui está um exemplo de função que implementa esses passos:

```js
const findConsecutive = (arr, n) =>
  arr.slice(n - 1).map((v, i) => arr.slice(i, i + n));
```

Você pode chamar esta função com um array e um número `n` para encontrar todos os arrays de `n` elementos consecutivos no array. Por exemplo:

```js
findConsecutive([1, 2, 3, 4, 5], 2);
// [[1, 2], [2, 3], [3, 4], [4, 5]]
```
