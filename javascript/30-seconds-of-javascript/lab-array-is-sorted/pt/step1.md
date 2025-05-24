# Prática de Código: Verificar se um Array está Ordenado

Para praticar a codificação, abra o Terminal/SSH e digite `node`.

Aqui está uma função para verificar se um array numérico está ordenado:

```js
const isSorted = (arr) => {
  if (arr.length <= 1) return 0;
  const direction = arr[1] - arr[0];
  for (let i = 2; i < arr.length; i++) {
    if ((arr[i] - arr[i - 1]) * direction < 0) return 0;
  }
  return Math.sign(direction);
};
```

Para usá-la, passe um array de números para `isSorted()`. A função retornará `1` se o array estiver ordenado em ordem ascendente, `-1` se estiver ordenado em ordem descendente e `0` se não estiver ordenado.

Aqui estão alguns exemplos:

```js
isSorted([0, 1, 2, 2]); // 1
isSorted([4, 3, 2]); // -1
isSorted([4, 3, 5]); // 0
isSorted([4]); // 0
```
