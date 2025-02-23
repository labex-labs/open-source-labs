# 非同期関数のチェーン化

非同期関数をチェーン化するには、ターミナル/SSH を開いて `node` と入力します。次に、非同期イベントを含む関数の配列をループし、各非同期イベントが完了したときに `next` 関数を呼び出します。

非同期関数をチェーン化する方法を示すコード スニペットは次のとおりです。

```js
const chainAsync = (fns) => {
  let curr = 0;
  const last = fns[fns.length - 1];
  const next = () => {
    const fn = fns[curr++];
    fn === last ? fn() : fn(next);
  };
  next();
};

chainAsync([
  (next) => {
    console.log("0 seconds");
    setTimeout(next, 1000);
  },
  (next) => {
    console.log("1 second");
    setTimeout(next, 1000);
  },
  () => {
    console.log("2 second");
  }
]);
```
