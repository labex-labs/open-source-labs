# 期間をフォーマットする

与えられたミリ秒数の読みやすい形式を取得するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `ms` を適切な値で割って、`day`、`hour`、`minute`、`second`、`millisecond` に適切な値を取得します。
3. `Object.entries()` と `Array.prototype.filter()` を使って、ゼロ以外の値のみを残します。
4. `Array.prototype.map()` を使って、各値に対する文字列を作成し、適切に複数形にする。
5. `Array.prototype.join()` を使って値を文字列に結合します。

以下がコードです。

```js
const formatDuration = (ms) => {
  if (ms < 0) ms = -ms;
  const time = {
    day: Math.floor(ms / 86400000),
    hour: Math.floor(ms / 3600000) % 24,
    minute: Math.floor(ms / 60000) % 60,
    second: Math.floor(ms / 1000) % 60,
    millisecond: Math.floor(ms) % 1000
  };
  return Object.entries(time)
    .filter((val) => val[1] !== 0)
    .map(([key, val]) => `${val} ${key}${val !== 1 ? "s" : ""}`)
    .join(", ");
};
```

以下はいくつかの例です。

```js
formatDuration(1001); // '1 second, 1 millisecond'
formatDuration(34325055574);
// '397 days, 6 hours, 44 minutes, 15 seconds, 574 milliseconds'
```
