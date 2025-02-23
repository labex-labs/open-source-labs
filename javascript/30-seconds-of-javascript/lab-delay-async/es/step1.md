# Cómo retrasar la ejecución de una función asincrónica en JavaScript

Para retrasar la ejecución de una función asincrónica en JavaScript, puedes utilizar la función `sleep` que se muestra a continuación, que devuelve una `Promise` que se resuelve después de un determinado tiempo. Aquí te presento un ejemplo de cómo retrasar la ejecución de una parte de una función `async` utilizando `sleep`:

```js
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function sleepyWork() {
  console.log("Voy a dormir durante 1 segundo.");
  await sleep(1000);
  console.log("Me he despertado después de 1 segundo.");
}
```

Para utilizar esta función, simplemente llama a `sleepyWork()` y la consola mostrará los mensajes con un retraso de 1 segundo entre ellos.
