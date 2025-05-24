# Como Obter um Elemento Aleatório de um Array em JavaScript

Para obter um elemento aleatório de um array em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Math.random()` para gerar um número aleatório entre 0 e 1.
3.  Multiplique o número aleatório pelo comprimento do array usando `Array.prototype.length`.
4.  Arredonde o resultado para o número inteiro mais próximo usando `Math.floor()`.
5.  Use o número arredondado como um índice para acessar um elemento aleatório do array.
6.  Este método também funciona com strings.

Aqui está um trecho de código que demonstra esta abordagem:

```js
const getRandomElement = (arr) => arr[Math.floor(Math.random() * arr.length)];
```

Você pode usar a função `getRandomElement` com qualquer array para obter um elemento aleatório. Por exemplo:

```js
getRandomElement([3, 7, 9, 11]); // 9
```
