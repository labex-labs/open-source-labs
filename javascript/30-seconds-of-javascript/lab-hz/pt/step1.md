# Cálculo da Frequência da Função

Para medir a frequência de execução de uma função por segundo (hz/hertz), use a função `hz`. Você pode fazer isso seguindo estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `performance.now()` para obter a diferença em milissegundos antes e depois do loop de iteração para calcular o tempo decorrido na execução da função `iterations` vezes.
3.  Converta milissegundos em segundos e divida pelo tempo decorrido para retornar o número de ciclos por segundo.
4.  Se você quiser usar o padrão de 100 iterações, omita o segundo argumento, `iterations`.

```js
const hz = (fn, iterations = 100) => {
  const before = performance.now();
  for (let i = 0; i < iterations; i++) fn();
  return (1000 * iterations) / (performance.now() - before);
};
```

Aqui está um exemplo de como usar a função `hz` para comparar o desempenho de duas funções que calculam a soma de um array de 10.000 números:

```js
const numbers = Array(10000)
  .fill()
  .map((_, i) => i);

const sumReduce = () => numbers.reduce((acc, n) => acc + n, 0);
const sumForLoop = () => {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) sum += numbers[i];
  return sum;
};

Math.round(hz(sumReduce)); // 572
Math.round(hz(sumForLoop)); // 4784
```

Neste exemplo, `sumReduce` é mais rápido que `sumForLoop` porque tem uma frequência de execução de função menor.
