# Como Achatar Profundamente um Array usando Recursão em JavaScript

Para achatar profundamente um array em JavaScript, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use recursão para achatar o array.
3. Use o método `Array.prototype.concat()` com um array vazio (`[]`) e o operador spread (`...`) para achatar o array.
4. Achate recursivamente cada elemento que for um array.
5. Implemente o seguinte código:

```js
const deepFlatten = (arr) =>
  [].concat(...arr.map((v) => (Array.isArray(v) ? deepFlatten(v) : v)));

deepFlatten([1, [2], [[3], 4], 5]); // [1, 2, 3, 4, 5]
```

Seguindo estes passos, você pode facilmente achatar profundamente um array usando recursão em JavaScript.
