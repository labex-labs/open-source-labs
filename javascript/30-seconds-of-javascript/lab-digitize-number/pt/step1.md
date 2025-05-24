# Como Digitalizar um Número

Para digitalizar um número em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Math.abs()` para remover o sinal do número.
3.  Converta o número em uma string e use o operador spread (`...`) para criar um array de dígitos.
4.  Use `Array.prototype.map()` e `parseInt()` para converter cada dígito em um inteiro.

Aqui está o código para a função `digitize`:

```js
const digitize = (n) => [...`${Math.abs(n)}`].map((i) => parseInt(i));
```

Exemplo de uso:

```js
digitize(123); // [1, 2, 3]
digitize(-123); // [1, 2, 3]
```
