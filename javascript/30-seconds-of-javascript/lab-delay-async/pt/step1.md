# Como Atrasar a Execução de uma Função Assíncrona em JavaScript

Para atrasar a execução de uma função assíncrona em JavaScript, você pode usar a função `sleep` abaixo, que retorna uma `Promise` que é resolvida após um certo período de tempo. Aqui está um exemplo de como atrasar a execução de parte de uma função `async` usando `sleep`:

```js
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function sleepyWork() {
  console.log("I'm going to sleep for 1 second.");
  await sleep(1000);
  console.log("I woke up after 1 second.");
}
```

Para usar esta função, simplesmente chame `sleepyWork()` e o console registrará as mensagens com um atraso de 1 segundo entre elas.
