# JavaScript で何日間前の日付を計算する関数

ここに、今日から `n` 日前の日付を計算し、`yyyy-mm-dd` 形式の文字列として返す JavaScript 関数があります。

```js
const daysAgo = (n) => {
  const today = new Date();
  const daysAgoDate = new Date(today.setDate(today.getDate() - Math.abs(n)));
  return daysAgoDate.toISOString().split("T")[0];
};
```

この関数の動作方法は以下の通りです。

- `Date` コンストラクタを使用して現在の日付を取得します。
- `Math.abs()` 関数を使用して、日数が正の数であることを確認します。
- `Date.prototype.getDate()` 関数を使用して、現在の日付の月の日を取得します。
- `Date.prototype.setDate()` 関数を使用して、日付を適切に更新します。
- 結果の日付は、`Date.prototype.toISOString()` 関数を使用して `yyyy-mm-dd` 形式の文字列として返されます。

使用例：

```js
daysAgo(20); // "2020-09-16" (現在の日付が 2020-10-06 の場合)
```
