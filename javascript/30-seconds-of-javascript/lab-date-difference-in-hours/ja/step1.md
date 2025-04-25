# 時間での日付の差分を計算する JavaScript 関数

JavaScript を使って 2 つの日付の差分を時間で計算するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。

2. 2 つの `Date` オブジェクト間の差分（時間で）を取得するには、次の JavaScript 関数を使用します。

```js
const getHoursDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600);
```

3. 2 つの日付を引数として関数を呼び出して、時間の差分を取得します。

```js
getHoursDiffBetweenDates(
  new Date("2021-04-24 10:25:00"),
  new Date("2021-04-25 10:25:00")
); // 24
```
