# Como Alternar um Elemento em um Array

Para alternar um elemento em um array, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Verifique se o elemento fornecido está no array usando `Array.prototype.includes()`.
3.  Se o elemento estiver no array, use `Array.prototype.filter()` para removê-lo.
4.  Se o elemento não estiver no array, use o operador spread (`...`) para adicioná-lo.
5.  Use a função `toggleElement`, que aceita um array e um valor, para alternar o elemento no array.

```js
const toggleElement = (arr, val) =>
  arr.includes(val) ? arr.filter((el) => el !== val) : [...arr, val];

toggleElement([1, 2, 3], 2); // [1, 3]
toggleElement([1, 2, 3], 4); // [1, 2, 3, 4]
```

Seguindo estes passos, você pode facilmente alternar um elemento em um array usando JavaScript.
