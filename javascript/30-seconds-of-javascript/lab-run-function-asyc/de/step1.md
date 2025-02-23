# Asynchrone Funktionsausführung mit Web Workers

Um eine Funktion auszuführen, ohne die Benutzeroberfläche zu blockieren, verwenden Sie einen Web Worker, um die Funktion in einem separaten Thread auszuführen. So geht es:

1. Erstellen Sie einen `Worker` mithilfe einer `Blob`-Objekt-URL, wobei der Inhalt die stringifizierte Version der auszuführenden Funktion ist.
2. Geben Sie sofort den Rückgabewert des aufgerufenen Funktionsaufrufs zurück.
3. Geben Sie ein `Promise` zurück, hören Sie auf `onmessage`- und `onerror`-Ereignisse und lösen Sie die von der Worker zurückgesendeten Daten auf, oder werfen Sie einen Fehler.

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

Beachten Sie, dass die an `runAsync` übergebene Funktion keine Closures verwenden sollte, da alles stringifiziert und zu einem Literal wird. Daher müssen alle Variablen und Funktionen innerhalb definiert werden. Hier sind einige Beispiele:

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
