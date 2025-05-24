# Encontrando a Interseção de Arrays

Para encontrar os elementos comuns entre dois arrays e remover duplicatas, use o seguinte código:

```js
const intersection = (arr1, arr2) => {
  const set = new Set(arr2);
  return [...new Set(arr1)].filter((elem) => set.has(elem));
};
```

Para usar este código, abra o Terminal/SSH e digite `node`. Em seguida, chame a função `intersection` com dois arrays como argumentos, assim:

```js
intersection([1, 2, 3], [4, 3, 2]); // [2, 3]
```

Isso retornará um array contendo os elementos que existem em ambos os arrays, com duplicatas removidas.
