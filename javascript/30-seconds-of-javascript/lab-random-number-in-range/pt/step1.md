# Como Gerar um Número Aleatório em um Intervalo Específico usando JavaScript

Para gerar um número aleatório em um intervalo especificado usando JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Math.random()` para gerar um valor aleatório.
3.  Mapeie o valor gerado para o intervalo desejado usando multiplicação.
4.  Use o seguinte código para criar uma função que gera um número aleatório no intervalo fornecido:

```js
const randomNumberInRange = (min, max) => Math.random() * (max - min) + min;
```

5.  Para usar a função, passe os valores mínimo e máximo do intervalo desejado como argumentos. Por exemplo:

```js
randomNumberInRange(2, 10); // 6.0211363285087005
```

Seguindo estes passos, você pode facilmente gerar um número aleatório em um intervalo específico usando JavaScript.
