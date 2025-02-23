# 分単位での日付差分を計算する関数

2つの日付の差分（分単位）を計算するには、次の関数を使用します。

```js
const getMinutesDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 60);
```

2つの`Date`オブジェクトを単純に引き算し、1分間のミリ秒数で割ることで、それらの間の差分（分単位）を取得します。

この関数の使用例は次のとおりです。

```js
getMinutesDiffBetweenDates(
  new Date("2021-04-24 01:00:15"),
  new Date("2021-04-24 02:00:15")
); // 60
```

コーディングの練習を始めるには、ターミナル/SSHを開き、`node`と入力します。
