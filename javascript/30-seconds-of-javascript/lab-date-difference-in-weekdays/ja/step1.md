# 2つの日付の間の平日を数える

2つの日付の間の平日を数えるには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングを練習するために `node` と入力します。
2. `Array.from()` を使って、`startDate` と `endDate` の間の日数と同じ長さの配列を作成します。
3. `Array.prototype.reduce()` を使って配列を反復処理し、各日付が平日かどうかを確認して `count` を増やします。
4. 各ループで `Date.prototype.getDate()` と `Date.prototype.setDate()` を使って `startDate` を次の日に更新し、1日進めます。
5. この関数は祝日を考慮していません。

これを実装するコードは次のとおりです。

```js
const countWeekDaysBetween = (startDate, endDate) =>
  Array.from({ length: (endDate - startDate) / (1000 * 3600 * 24) }).reduce(
    (count) => {
      if (startDate.getDay() % 6 !== 0) count++;
      startDate = new Date(startDate.setDate(startDate.getDate() + 1));
      return count;
    },
    0
  );
```

この関数をテストするには、次のコードを使えます。

```js
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 06, 2020")); // 1
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 14, 2020")); // 7
```
