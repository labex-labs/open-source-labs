# Gerando Números Aleatórios Gaussianos usando a Transformação de Box-Muller

Para gerar números aleatórios gaussianos (normalmente distribuídos) usando a transformação de Box-Muller, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o trecho de código fornecido que utiliza a transformação de Box-Muller para gerar números aleatórios com uma distribuição gaussiana.
3.  A função `randomGauss()` fornecida no trecho de código gera um número aleatório com uma distribuição gaussiana.
4.  A saída da função `randomGauss()` é um número entre 0 e 1.
5.  A saída pode ser usada para várias aplicações, como simulações estatísticas, análise de dados e aprendizado de máquina.

```js
const randomGauss = () => {
  const theta = 2 * Math.PI * Math.random();
  const rho = Math.sqrt(-2 * Math.log(1 - Math.random()));
  return (rho * Math.cos(theta)) / 10.0 + 0.5;
};
```

Exemplo de Uso:

```js
randomGauss(); // 0.5
```
