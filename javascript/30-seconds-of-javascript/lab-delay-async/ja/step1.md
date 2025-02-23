# JavaScript における非同期関数の実行を遅延させる方法

JavaScript において非同期関数の実行を遅延させるには、以下の `sleep` 関数を使用できます。この関数は一定時間経過後に解決する `Promise` を返します。以下は、`sleep` を使って `async` 関数の一部の実行を遅延させる方法の例です。

```js
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function sleepyWork() {
  console.log("I'm going to sleep for 1 second.");
  await sleep(1000);
  console.log("I woke up after 1 second.");
}
```

この関数を使用するには、単に `sleepyWork()` を呼び出します。そうすると、コンソールにはメッセージが表示され、それらの間に 1 秒間の遅延があります。
