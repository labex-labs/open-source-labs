# Como Inicializar um Array até que uma Condição seja Atendida

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Aqui estão os passos para inicializar e preencher um array com valores gerados por uma função até que uma determinada condição seja atendida:

1. Crie um array vazio `arr`, uma variável de índice `i` e um elemento `el`.
2. Use um loop `do...while` para adicionar elementos ao array usando a função `mapFn` até que a função `conditionFn` retorne `true` para o índice `i` e o elemento `el` dados.
3. A função `conditionFn` recebe três argumentos: o índice atual, o elemento anterior e o próprio array.
4. A função `mapFn` recebe três argumentos: o índice atual, o elemento atual e o próprio array.

Aqui está o código:

```js
const initializeArrayUntil = (conditionFn, mapFn) => {
  const arr = [];
  let i = 0;
  let el = undefined;
  do {
    el = mapFn(i, el, arr);
    arr.push(el);
    i++;
  } while (!conditionFn(i, el, arr));
  return arr;
};
```

Para usar a função `initializeArrayUntil`, forneça duas funções como argumentos:

```js
initializeArrayUntil(
  (i, val) => val > 10, //conditionFn
  (i, val, arr) => (i <= 1 ? 1 : val + arr[i - 2]) //mapFn
); // [1, 1, 2, 3, 5, 8, 13]
```

Este código inicializa um array com a sequência de Fibonacci até o primeiro número maior que 10. A função `conditionFn` verifica se o valor atual é maior que 10, e a função `mapFn` gera o próximo número na sequência.
