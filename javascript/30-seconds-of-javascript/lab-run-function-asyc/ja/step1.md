# Web Worker を使った非同期関数の実行

UI をブロックすることなく関数を実行するには、Web Worker を使って関数を別のスレッドで実行します。方法は以下の通りです。

1. 実行する関数の文字列化されたバージョンを内容とする `Blob` オブジェクト URL を使って `Worker` を作成します。
2. 関数を呼び出した結果を即座に返します。
3. `onmessage` と `onerror` イベントを待ち、ワーカーから返されたデータを解決するか、エラーを投げる `Promise` を返します。

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

`runAsync` に渡される関数はクロージャを使用しないでください。なぜならすべてが文字列化されてリテラルになるからです。したがって、すべての変数と関数は内部で定義する必要があります。以下にいくつかの例を示します。

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
