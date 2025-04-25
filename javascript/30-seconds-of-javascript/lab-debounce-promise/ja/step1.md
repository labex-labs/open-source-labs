# デバウンスプロミス

プロミスを返すデバウンス関数を作成し、前回呼び出されてから少なくとも `ms` ミリ秒が経過するまで、提供された関数の呼び出しを遅らせるには、次の手順を使用します。

1. デバウンス関数が呼び出されるたびに、`clearTimeout()` で現在の保留中のタイムアウトをクリアし、その後 `setTimeout()` を使用して、関数の呼び出しを少なくとも `ms` ミリ秒が経過するまで遅らせる新しいタイムアウトを作成します。
2. `Function.prototype.apply()` を使用して、`this` コンテキストを関数に適用し、必要な引数を提供します。
3. 新しい `Promise` を作成し、その `resolve` と `reject` コールバックを保留中のプロミスのスタックに追加します。
4. `setTimeout()` が呼び出されたとき、現在のスタックをコピーします（提供された関数の呼び出しとその解決の間で変更される可能性があるため）、それをクリアしてから提供された関数を呼び出します。
5. 提供された関数が解決/拒否したとき、返されたデータでスタック内のすべてのプロミス（関数が呼び出されたときにコピーされたもの）を解決/拒否します。
6. 2 番目の引数 `ms` を省略すると、タイムアウトを既定の `0` ms に設定します。

以下は、`debouncePromise()` 関数のコードです。

```js
const debouncePromise = (fn, ms = 0) => {
  let timeoutId;
  const pending = [];
  return (...args) =>
    new Promise((res, rej) => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => {
        const currentPending = [...pending];
        pending.length = 0;
        Promise.resolve(fn.apply(this, args)).then(
          (data) => {
            currentPending.forEach(({ resolve }) => resolve(data));
          },
          (error) => {
            currentPending.forEach(({ reject }) => reject(error));
          }
        );
      }, ms);
      pending.push({ resolve: res, reject: rej });
    });
};
```

以下は、`debouncePromise()` を使用する方法の例です。

```js
const fn = (arg) =>
  new Promise((resolve) => {
    setTimeout(resolve, 1000, ["resolved", arg]);
  });
const debounced = debouncePromise(fn, 200);
debounced("foo").then(console.log);
debounced("bar").then(console.log);
// 両方の場合に ['resolved', 'bar'] をコンソールに表示します
```
