# 今日から `n` 日後の日付を計算する関数

今日から `n` 日後の日付を計算するには、次の手順に従います。

- ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
- `Date` コンストラクタを使って現在の日付を取得します。
- `Math.abs()` と `Date.prototype.getDate()` を使って日付を適切に更新します。
- `Date.prototype.setDate()` を使って結果を設定します。
- `Date.prototype.toISOString()` を使って `yyyy-mm-dd` 形式の文字列を返します。

以下がコードです。

```js
const daysFromNow = (n) => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + Math.abs(n));
  return currentDate.toISOString().split("T")[0];
};
```

使用例：

```js
daysFromNow(5); // 出力：2020-10-13 (現在の日付が 2020-10-08 の場合)
```
