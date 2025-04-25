# 日付の差を日数で計算する関数

2 つの日付の間の差を日数で計算するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために`node`と入力します。
2. 2 つの`Date`オブジェクトを引数として`getDaysDiffBetweenDates`関数を使用します。
3. この関数は、最終日付から初期日付を引き、その結果を 1 日のミリ秒数で割って、それらの間の日数の差を取得します。

以下は、`getDaysDiffBetweenDates`関数のコードです。

```js
const getDaysDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600 * 24);
```

この関数を使用するには、`YYYY-MM-DD`形式の 2 つの`Date`オブジェクトを渡します。

```js
getDaysDiffBetweenDates(new Date("2017-12-13"), new Date("2017-12-22")); // 9
```

これは、2 つの日付の間の差を日数で返し、この例では 9 になります。
