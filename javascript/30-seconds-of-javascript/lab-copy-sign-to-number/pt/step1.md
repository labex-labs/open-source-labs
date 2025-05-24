# Função para Copiar o Sinal de um Número para Outro

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

A função `copySign` retorna o valor absoluto do primeiro número, mas com o sinal do segundo número. Para realizar isso:

1. Use `Math.sign()` para verificar se os dois números têm o mesmo sinal.
2. Retorne `x` se tiverem, `-x` caso contrário.

Aqui está o código para a função `copySign`:

```js
const copySign = (x, y) => (Math.sign(x) === Math.sign(y) ? x : -x);
```

Você pode testar a função usando o seguinte código:

```js
copySign(2, 3); // 2
copySign(2, -3); // -2
copySign(-2, 3); // 2
copySign(-2, -3); // -2
```
