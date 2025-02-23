# Ejecución de funciones asíncronas con Web Workers

Para ejecutar una función sin bloquear la interfaz de usuario, utiliza un Web Worker para ejecutar la función en un hilo separado. Aquí está cómo:

1. Crea un `Worker` utilizando una URL de objeto `Blob`, con el contenido siendo la versión serializada de la función que se va a ejecutar.
2. Immediatamente devuelve el valor de retorno de llamar a la función de vuelta.
3. Devuelve una `Promise`, escuchando los eventos `onmessage` y `onerror` y resolviendo los datos devueltos por el worker, o lanzando un error.

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

Tenga en cuenta que la función suministrada a `runAsync` no debe utilizar closures porque todo se serializa y se convierte en literal. Por lo tanto, todas las variables y funciones deben definirse dentro. Aquí hay algunos ejemplos:

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
