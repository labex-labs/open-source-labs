# アニメーションフレームの記録ガイド

アニメーションフレームを記録するには、以下の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. 再帰を使って、各アニメーションフレームで提供されたコールバックを呼び出します。
3. `running` が `true` の場合、`Window.requestAnimationFrame()` を続けて呼び出します。これは提供されたコールバックを呼び出します。
4. 記録の手動制御を可能にするには、`start` と `stop` の 2 つのメソッドを持つオブジェクトを返します。
5. 関数が呼び出されたときに `start` を暗黙的に呼び出すために、2 番目の引数 `autoStart` を省略します。

アニメーションフレームを記録するには、次のコードを使用します。

```js
const recordAnimationFrames = (callback, autoStart = true) => {
  let running = false,
    raf;
  const stop = () => {
    if (!running) return;
    running = false;
    cancelAnimationFrame(raf);
  };
  const start = () => {
    if (running) return;
    running = true;
    run();
  };
  const run = () => {
    raf = requestAnimationFrame(() => {
      callback();
      if (running) run();
    });
  };
  if (autoStart) start();
  return { start, stop };
};
```

コードの使用例：

```js
const cb = () => console.log("Animation frame fired");
const recorder = recordAnimationFrames(cb);
// 各アニメーションフレームで 'Animation frame fired' をログに出力します
recorder.stop(); // ログ出力を停止します
recorder.start(); // 再開します
const recorder2 = recordAnimationFrames(cb, false);
// フレームの記録を開始するには、明示的に `start` を呼び出す必要があります
```
