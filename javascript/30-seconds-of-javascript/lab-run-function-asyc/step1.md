# Asynchronous Function Execution Using Web Workers

To execute a function without blocking the UI, use a Web Worker to run the function in a separate thread. Here's how:

1. Create a `Worker` using a `Blob` object URL, with the contents being the stringified version of the function to be executed.
2. Immediately post the return value of calling the function back.
3. Return a `Promise`, listening for `onmessage` and `onerror` events and resolving the data posted back from the worker, or throwing an error.

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

Note that the function supplied to `runAsync` should not use closures because everything gets stringified and becomes literal. Therefore, all variables and functions must be defined inside. Here are some examples:

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
