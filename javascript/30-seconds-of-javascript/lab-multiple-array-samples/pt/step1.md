# Prática de Código: Obtendo Elementos Aleatórios de um Array

Para praticar a codificação, abra o Terminal/SSH e digite `node`. O código a seguir utiliza o algoritmo Fisher-Yates para embaralhar um array e recuperar `n` elementos aleatórios e únicos em chaves únicas do array, até o tamanho do array.

```js
const sampleSize = ([...arr], n = 1) => {
  let m = arr.length;
  while (m) {
    const i = Math.floor(Math.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  }
  return arr.slice(0, n);
};
```

Para usar este código, chame `sampleSize()` com um array e um número opcional `n` de elementos a serem recuperados. Se `n` não for fornecido, a função retornará apenas um elemento aleatório do array.

```js
sampleSize([1, 2, 3], 2); // [3, 1]
sampleSize([1, 2, 3], 4); // [2, 3, 1]
```
