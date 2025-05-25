# Como Gerar um Inteiro Aleatório em um Intervalo Específico Usando JavaScript

Para gerar um inteiro aleatório em um intervalo especificado usando JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Math.random()` para gerar um número aleatório entre 0 e 1.
3.  Mapeie o número aleatório para o intervalo desejado, multiplicando-o pela diferença entre os valores máximo e mínimo do intervalo e, em seguida, adicionando o valor mínimo ao resultado.
4.  Use o método `Math.floor()` para arredondar o resultado para baixo para o inteiro mais próximo.

Aqui está um trecho de código de exemplo que implementa os passos acima:

```js
const randomIntegerInRange = (min, max) =>
  Math.floor(Math.random() * (max - min + 1)) + min;
```

Você pode então chamar a função `randomIntegerInRange()` com os valores mínimo e máximo desejados para gerar um inteiro aleatório dentro desse intervalo. Por exemplo:

```js
randomIntegerInRange(0, 5); // 2
```
