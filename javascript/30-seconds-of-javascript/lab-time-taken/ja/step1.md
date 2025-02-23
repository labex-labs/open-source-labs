# 関数の実行にかかる時間の測定

関数の実行にかかる時間を測定するには、`console.time()` と `console.timeEnd()` を使って開始時刻と終了時刻の差を求めます。

次に、コールバック関数の実行にかかる時間を測定する `timeTaken` という関数の例を示します。

```js
const timeTaken = (callback) => {
  console.time("timeTaken");
  const result = callback();
  console.timeEnd("timeTaken");
  return result;
};
```

この関数を使用するには、コールバックを引数として渡します。たとえば：

```js
timeTaken(() => Math.pow(2, 10)); // Returns 1024, and logs: timeTaken: 0.02099609375ms
```

上記の例では、`timeTaken` 関数を使って `Math.pow(2, 10)` 関数呼び出しの実行にかかる時間を測定しています。この関数呼び出しは 1024 を返します。コンソール出力には、ミリ秒 (ms) で測定された時間が表示されます。
