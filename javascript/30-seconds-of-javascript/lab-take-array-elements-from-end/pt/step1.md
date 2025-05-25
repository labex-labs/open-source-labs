# Como Remover Elementos de um Array do Final em JavaScript

Para remover elementos do final de um array em JavaScript, você pode usar o método `Array.prototype.slice()`. Veja como você pode fazer isso:

```js
const takeRight = (arr, n = 1) => arr.slice(arr.length - n, arr.length);
```

Esta função cria um novo array com os últimos `n` elementos do array original. Veja como você pode usá-la:

```js
takeRight([1, 2, 3], 2); // [ 2, 3 ]
takeRight([1, 2, 3]); // [3]
```

Para usar esta função, abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
