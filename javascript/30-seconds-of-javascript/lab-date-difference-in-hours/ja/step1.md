# 時間での日付の差分を計算するJavaScript関数

JavaScriptを使って2つの日付の差分を時間で計算するには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングを練習するために `node` と入力します。

2. 2つの `Date` オブジェクト間の差分（時間で）を取得するには、次のJavaScript関数を使用します。

```js
const getHoursDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600);
```

3. 2つの日付を引数として関数を呼び出して、時間の差分を取得します。

```js
getHoursDiffBetweenDates(
  new Date("2021-04-24 10:25:00"),
  new Date("2021-04-25 10:25:00")
); // 24
```
