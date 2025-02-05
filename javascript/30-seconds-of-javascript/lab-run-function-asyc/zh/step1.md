# 使用 Web Workers 进行异步函数执行

要在不阻塞用户界面的情况下执行函数，请使用 Web Worker 在单独的线程中运行该函数。具体方法如下：

1. 使用 `Blob` 对象 URL 创建一个 `Worker`，其内容为要执行函数的字符串化版本。
2. 立即回调调用该函数的返回值。
3. 返回一个 `Promise`，监听 `onmessage` 和 `onerror` 事件，并解析从 worker 发回的数据，或者抛出错误。

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

请注意，提供给 `runAsync` 的函数不应使用闭包，因为所有内容都会被字符串化并变成字面量。因此，所有变量和函数都必须在内部定义。以下是一些示例：

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
