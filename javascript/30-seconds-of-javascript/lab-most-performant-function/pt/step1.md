# Como Encontrar a Função de Maior Desempenho em JavaScript

Para encontrar a função de maior desempenho em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.map()` para gerar um array onde cada valor é o tempo total gasto para executar a função após `iterations` vezes.
3.  Use a diferença nos valores de `performance.now()` antes e depois para obter o tempo total em milissegundos com um alto grau de precisão.
4.  Use `Math.min()` para encontrar o tempo de execução mínimo e retorne o índice desse tempo mais curto, que corresponde ao índice da função de maior desempenho.
5.  Se você omitir o segundo argumento, `iterations`, a função usará um padrão de `10000` iterações.
6.  Tenha em mente que quanto mais iterações você usar, mais confiável será o resultado, mas levará mais tempo.

Aqui está um trecho de código de exemplo:

```js
const mostPerformant = (fns, iterations = 10000) => {
  const times = fns.map((fn) => {
    const before = performance.now();
    for (let i = 0; i < iterations; i++) fn();
    return performance.now() - before;
  });
  return times.indexOf(Math.min(...times));
};
```

Para usar esta função, passe um array de funções como o primeiro argumento e o número de iterações como o segundo argumento (opcional). Por exemplo:

```js
mostPerformant([
  () => {
    // Loops through the entire array before returning `false`
    [1, 2, 3, 4, 5, 6, 7, 8, 9, "10"].every((el) => typeof el === "number");
  },
  () => {
    // Only needs to reach index `1` before returning `false`
    [1, "2", 3, 4, 5, 6, 7, 8, 9, 10].every((el) => typeof el === "number");
  }
]); // 1
```
