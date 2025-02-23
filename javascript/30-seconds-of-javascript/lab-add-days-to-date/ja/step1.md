# 日付に日数を追加する関数

与えられた日付から `n` 日後の日付を計算し、その文字列を返す関数がここにあります。

この関数を使用するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. 最初の引数から `Date` オブジェクトを作成するために `Date` コンストラクタを使用します。
3. `Date.prototype.getDate()` と `Date.prototype.setDate()` を使用して、与えられた日付に `n` 日を追加します。
4. `Date.prototype.toISOString()` を使用して `yyyy-mm-dd` 形式の文字列を返します。

ここに関数のコードがあります。

```js
const addDaysToDate = (date, n) => {
  const d = new Date(date);
  d.setDate(d.getDate() + n);
  return d.toISOString().split("T")[0];
};
```

次の例を使用して関数をテストできます。

```js
addDaysToDate("2020-10-15", 10); // '2020-10-25'
addDaysToDate("2020-10-15", -10); // '2020-10-05'
```
