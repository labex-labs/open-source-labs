# Algoritmo de Busca Linear (Linear Search Algorithm)

Para praticar a codificação, abra o Terminal ou SSH e digite `node`. O algoritmo de busca linear encontra o primeiro índice de um elemento dado em um array.

Veja como funciona:

- Use um loop `for...in` para iterar sobre os índices do array fornecido.
- Verifique se o elemento no índice correspondente é igual a `item`.
- Se o elemento for encontrado, retorne o índice. Use o operador unário `+` para convertê-lo de uma string para um número.
- Se o elemento não for encontrado após iterar sobre todo o array, retorne `-1`.

Aqui está o código:

```js
const linearSearch = (arr, item) => {
  for (const i in arr) {
    if (arr[i] === item) return +i;
  }
  return -1;
};
```

Para testar a função, chame-a com um array e um valor para pesquisar:

```js
linearSearch([2, 9, 9], 9); // 1
linearSearch([2, 9, 9], 7); // -1
```
