# Medindo o Tempo de Execução de uma Função

Para medir o tempo de execução de uma função, use `console.time()` e `console.timeEnd()` para determinar a diferença entre os tempos de início e fim.

Aqui está um exemplo de função chamada `timeTaken` que mede o tempo de execução de uma função de callback:

```js
const timeTaken = (callback) => {
  console.time("timeTaken");
  const result = callback();
  console.timeEnd("timeTaken");
  return result;
};
```

Para usar esta função, basta passar seu callback como um argumento. Por exemplo:

```js
timeTaken(() => Math.pow(2, 10)); // Returns 1024, and logs: timeTaken: 0.02099609375ms
```

No exemplo acima, a função `timeTaken` é usada para medir o tempo gasto na execução da chamada da função `Math.pow(2, 10)`, que retorna 1024. A saída do console mostrará o tempo gasto em milissegundos (ms).
