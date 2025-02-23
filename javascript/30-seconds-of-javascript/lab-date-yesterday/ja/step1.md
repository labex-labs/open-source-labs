# yyyy - mm - dd 形式で昨日の日付を取得する

`yyyy - mm - dd` 形式で昨日の日付を取得するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `Date` コンストラクタを使用して現在の日付を取得します。
3. `Date.prototype.getDate()` を使用して日付を 1 日減らします。
4. `Date.prototype.setDate()` を使用して減算した日付を設定します。
5. `Date.prototype.toISOString()` を使用して `yyyy - mm - dd` 形式の文字列を返します。
6. `yesterday()` 関数を呼び出して昨日の日付を取得します。

```js
const yesterday = () => {
  let d = new Date();
  d.setDate(d.getDate() - 1);
  return d.toISOString().split("T")[0];
};

yesterday(); // 現在の日付が 2018 - 10 - 18 の場合、"2018 - 10 - 17" を返す
```

これらの手順に従えば、明確かつ簡潔に昨日の日付を取得することができます。
