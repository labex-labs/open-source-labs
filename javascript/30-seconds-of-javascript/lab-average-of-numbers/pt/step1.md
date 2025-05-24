# Como Calcular a Média de Números em JavaScript

Para calcular a média de dois ou mais números em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método embutido `Array.prototype.reduce()` para adicionar cada valor a um acumulador, inicializado com o valor `0`.
3.  Divida a soma resultante pelo comprimento do array.

Aqui está um exemplo de trecho de código que você pode usar:

```js
const average = (...nums) =>
  nums.reduce((acc, val) => acc + val, 0) / nums.length;
```

Você pode chamar a função `average` com um array ou múltiplos argumentos:

```js
average(...[1, 2, 3]); // 2
average(1, 2, 3); // 2
```
