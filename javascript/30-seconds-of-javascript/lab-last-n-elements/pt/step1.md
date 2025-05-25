# Como Obter os Últimos N Elementos de um Array em JavaScript

Para obter os últimos `n` elementos de um array em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

2.  Use `Array.prototype.slice()` com um valor inicial de `-n` para obter os últimos `n` elementos do array.

Aqui está o código JavaScript para obter os últimos `n` elementos de um array:

```js
const lastN = (arr, n) => arr.slice(-n);
```

Para testar o código, chame a função `lastN()` com o array e o número de elementos que você deseja obter, assim:

```js
lastN(["a", "b", "c", "d"], 2); // ['c', 'd']
```
