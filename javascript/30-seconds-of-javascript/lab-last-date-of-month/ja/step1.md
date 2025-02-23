# 月の最終日を返す関数

コーディングを始めるには、ターミナル/SSH を開いて `node` と入力します。

この関数は、指定された日付の月の最終日を返します。

これを達成するには、次の手順に従います。

1. `Date.prototype.getFullYear()` と `Date.prototype.getMonth()` を使って、指定された日付から現在の年と月を取得します。
2. 与えられた年と月に `1` を加え、日付を `0` に設定した新しい日付を作成します（前月の最終日）。この目的で `Date` コンストラクタを使うことができます。
3. 関数に引数が渡されない場合、デフォルトで現在の日付を使用します。
4. 月の最終日を日付の文字列形式で返します。

ここに関数のコードを示します。

```js
const getLastDateOfMonth = (date = new Date()) => {
  let lastDate = new Date(date.getFullYear(), date.getMonth() + 1, 0);
  return lastDate.toISOString().split("T")[0];
};
```

この関数を、日付オブジェクトを使って呼び出すことでテストすることができます。

```js
getLastDateOfMonth(new Date("2015-08-11")); // '2015-08-30'
```
