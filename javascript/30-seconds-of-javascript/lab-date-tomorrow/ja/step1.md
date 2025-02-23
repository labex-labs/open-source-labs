# 明日の日付を取得する

コーディングを練習するには、まずターミナル/SSHを開き、`node`と入力します。これを行ったら、次の手順で明日の日付を取得できます。

1. `Date`コンストラクタを使用して現在の日付を取得します。
2. `Date.prototype.getDate()`を使用して1日増やします。
3. `Date.prototype.setDate()`を使用して結果を設定します。
4. `Date.prototype.toISOString()`を使用して`yyyy-mm-dd`形式の文字列を返します。

使用できるコードは次のとおりです。

```js
const tomorrow = () => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + 1);
  return currentDate.toISOString().split("T")[0];
};
```

このコードを入力したら、関数`tomorrow()`を呼び出すことで明日の日付を取得できます。たとえば、今日の日付が2018-10-18の場合、出力は`2018-10-19`になります。
