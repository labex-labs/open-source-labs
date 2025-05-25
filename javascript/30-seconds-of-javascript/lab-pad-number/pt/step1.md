# Como Preencher um Número em JavaScript

Para preencher um número em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `String.prototype.padStart()` para preencher o número para o comprimento especificado, após convertê-lo em uma string.
3.  A função `padNumber()` abaixo demonstra essa abordagem.
4.  Passe o número e o comprimento desejado como argumentos para a função.
5.  A função retorna o número preenchido como uma string.

```js
const padNumber = (n, l) => `${n}`.padStart(l, "0");
```

Exemplo de uso:

```js
padNumber(1234, 6); // '001234'
```
