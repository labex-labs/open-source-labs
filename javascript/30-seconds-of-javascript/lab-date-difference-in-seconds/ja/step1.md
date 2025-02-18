# 日付の差を秒単位で計算する関数

2つの日付の差を秒単位で計算するには、以下の手順に従ってください。

1. ターミナル/SSH を開き、`node` と入力してコーディングの練習を開始します。
2. 2つの `Date` オブジェクトを引き算し、1秒のミリ秒数で割ります。
3. その結果が2つの日付の差（秒単位）になります。

この計算を行う JavaScript 関数は次のとおりです。

```js
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;
```

この関数を使用するには、2つの `Date` オブジェクトを引数として渡します。次のようになります。

```js
getSecondsDiffBetweenDates(
  new Date("2020-12-24 00:00:15"),
  new Date("2020-12-24 00:00:17")
); // 2
```
