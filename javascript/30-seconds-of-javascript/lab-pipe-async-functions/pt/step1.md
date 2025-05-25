# Como Encadeiar Funções Assíncronas em JavaScript

Para começar a praticar a codificação com JavaScript, abra o Terminal/SSH e digite `node`. Depois de se familiarizar com o básico, você pode começar a trabalhar com funções assíncronas.

A função `pipeAsyncFunctions` permite que você execute a composição de funções da esquerda para a direita com funções assíncronas. Veja como funciona:

- A função recebe qualquer número de funções assíncronas como argumentos.
- O operador spread (`...`) é usado para passar essas funções como argumentos separados para a função `pipeAsyncFunctions`.
- A função resultante pode aceitar qualquer número de argumentos, mas cada uma das funções que estão sendo compostas deve aceitar um único argumento.
- As funções podem retornar uma combinação de valores normais, Promises, ou ser `async` e retornar através de `await`.
- O método `reduce()` é usado junto com `Promise.prototype.then()` para realizar a composição de funções.
- O método `reduce()` itera sobre as funções, executando cada uma em sequência e passando o resultado de uma função para a próxima.
- A Promise resultante é retornada.

Aqui está um exemplo de como usar `pipeAsyncFunctions` para somar um número:

```js
const sum = pipeAsyncFunctions(
  (x) => x + 1,
  (x) => new Promise((resolve) => setTimeout(() => resolve(x + 2), 1000)),
  (x) => x + 3,
  async (x) => (await x) + 4
);
(async () => {
  console.log(await sum(5)); // 15 (after one second)
})();
```

Neste exemplo, `sum` é composto por quatro funções que adicionam valores diferentes ao número de entrada. O valor final de `sum` é o resultado da execução de cada função em sequência, com um atraso de um segundo para a segunda função. A palavra-chave `async` é usada com a última função para permitir o uso de `await`.

Ao usar `pipeAsyncFunctions`, você pode facilmente compor qualquer número de funções assíncronas para criar funcionalidades mais complexas.
