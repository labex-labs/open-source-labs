# Como Inicializar e Preencher um Array com um Loop While em JavaScript

Para começar a praticar a codificação em JavaScript, abra o Terminal/SSH e digite `node`.

A função `initializeArrayWhile` inicializa e preenche um array com valores gerados por uma função enquanto uma condição é atendida. Veja como funciona:

1.  Crie um array vazio chamado `arr`, uma variável de índice chamada `i` e um elemento chamado `el`.
2.  Use um loop `while` para adicionar elementos ao array usando a função `mapFn`, desde que a função `conditionFn` retorne `true` para o índice `i` e o elemento `el` fornecidos.
3.  A função `conditionFn` recebe três argumentos: o índice atual, o elemento anterior e o próprio array.
4.  A função `mapFn` recebe três argumentos: o índice atual, o elemento atual e o próprio array.
5.  A função `initializeArrayWhile` retorna o array.

Aqui está o código:

```js
const initializeArrayWhile = (conditionFn, mapFn) => {
  const arr = [];
  let i = 0;
  let el = mapFn(i, undefined, arr);
  while (conditionFn(i, el, arr)) {
    arr.push(el);
    i++;
    el = mapFn(i, el, arr);
  }
  return arr;
};
```

Você pode usar a função `initializeArrayWhile` para inicializar e preencher um array com valores. Por exemplo:

```js
initializeArrayWhile(
  (i, val) => val < 10,
  (i, val, arr) => (i <= 1 ? 1 : val + arr[i - 2])
); // [1, 1, 2, 3, 5, 8]
```
