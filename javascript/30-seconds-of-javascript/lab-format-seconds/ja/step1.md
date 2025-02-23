# 秒数を ISO 時間形式にフォーマットする関数

このコードを使用するには、ターミナル/SSH を開いて `node` と入力します。この関数は、秒数を引数として受け取り、ISO 時間形式を返します。その動作方法は以下の通りです。

- 秒数を適切な値で割って、`hour`、`minute`、`second` に対応する値を取得します。
- 数値の符号を変数に格納して、結果の先頭に付けます。
- `Array.prototype.map()` を `Math.floor()` と `String.prototype.padStart()` と組み合わせて、各セグメントを文字列化してフォーマットします。
- `Array.prototype.join()` を使用して値を文字列に結合します。

以下がコードです。

```js
const formatSeconds = (s) => {
  const [hour, minute, second, sign] =
    s > 0
      ? [s / 3600, (s / 60) % 60, s % 60, ""]
      : [-s / 3600, (-s / 60) % 60, -s % 60, "-"];

  return (
    sign +
    [hour, minute, second]
      .map((v) => `${Math.floor(v)}`.padStart(2, "0"))
      .join(":")
  );
};
```

これらの例で関数をテストできます。

```js
formatSeconds(200); // '00:03:20'
formatSeconds(-200); // '-00:03:20'
formatSeconds(99999); // '27:46:39'
```
