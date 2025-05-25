# Execução de Funções Assíncronas Usando Web Workers

Para executar uma função sem bloquear a UI, use um Web Worker para executar a função em uma thread separada. Veja como:

1.  Crie um `Worker` usando uma URL de objeto `Blob`, com o conteúdo sendo a versão stringificada da função a ser executada.
2.  Poste imediatamente o valor de retorno da chamada da função de volta.
3.  Retorne uma `Promise`, ouvindo os eventos `onmessage` e `onerror` e resolvendo os dados postados de volta do worker, ou lançando um erro.

```js
const runAsync = (fn) => {
  const worker = new Worker(
    URL.createObjectURL(new Blob([`postMessage((${fn})());`]), {
      type: "application/javascript; charset=utf-8"
    })
  );
  return new Promise((resolve, reject) => {
    worker.onmessage = ({ data }) => {
      resolve(data);
      worker.terminate();
    };
    worker.onerror = (error) => {
      reject(error);
      worker.terminate();
    };
  });
};
```

Observe que a função fornecida para `runAsync` não deve usar closures porque tudo é stringificado e se torna literal. Portanto, todas as variáveis e funções devem ser definidas internamente. Aqui estão alguns exemplos:

```js
const longRunningFunction = () => {
  let result = 0;
  for (let i = 0; i < 1000; i++)
    for (let j = 0; j < 700; j++)
      for (let k = 0; k < 300; k++) result = result + i + j + k;

  return result;
};

runAsync(longRunningFunction).then(console.log); // 209685000000
runAsync(() => 10 ** 3).then(console.log); // 1000
let outsideVariable = 50;
runAsync(() => typeof outsideVariable).then(console.log); // 'undefined'
```
