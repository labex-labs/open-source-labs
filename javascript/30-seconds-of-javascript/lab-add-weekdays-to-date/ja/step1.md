# 与えられた日付に営業日を追加する関数

与えられた営業日数を追加して将来の日付を計算するには、`addWeekDays`関数を使用できます。手順は以下の通りです。

1. ターミナル/SSH を開き、コーディングを練習するために`node`と入力します。
2. `startDate`と`count`の 2 つの引数を持つ`addWeekDays`関数を使用します。
3. `startDate`は、営業日を追加し始める日付です。
4. `count`は、開始日付に追加する営業日数です。
5. 関数は`Array.from()`メソッドを使用して配列を構築し、追加する営業日数の`count`に等しい長さを設定します。
6. `Array.prototype.reduce()`メソッドを使用して、配列を`startDate`から反復処理し、`Date.prototype.getDate()`と`Date.prototype.setDate()`を使用してインクリメントします。
7. 関数は、現在の`date`が週末であるかどうかを確認します。
8. 現在の`date`が週末である場合、関数はそれを平日にするために 1 日または 2 日を追加して再度更新します。
9. 関数は祝日を考慮していません。

```js
const addWeekDays = (startDate, count) =>
  Array.from({ length: count }).reduce((date) => {
    date = new Date(date.setDate(date.getDate() + 1));
    if (date.getDay() % 6 === 0)
      date = new Date(date.setDate(date.getDate() + (date.getDay() / 6 + 1)));
    return date;
  }, startDate);
```

`addWeekDays`関数を使用する方法のいくつかの例を以下に示します。

```js
addWeekDays(new Date("Oct 09, 2020"), 5); // 'Oct 16, 2020'
addWeekDays(new Date("Oct 12, 2020"), 5); // 'Oct 19, 2020'
```
