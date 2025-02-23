# JavaScript の Date オブジェクトを使って 1 年の何日目を取得する方法

JavaScript の `Date` オブジェクトから 1 年の何日目（1 から 366 の数値）を取得するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Date` コンストラクタと `Date.prototype.getFullYear()` を使って、1 年の初日を `Date` オブジェクトとして取得します。
3. 1 年の初日を `date` オブジェクトから引き、1 日のミリ秒数で割って結果を取得します。
4. `Math.floor()` を使って、得られた日数を整数に丸めます。

以下がコードです。

```js
const dayOfYear = (date) =>
  Math.floor((date - new Date(date.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24);
```

この関数をテストするには、`Date` オブジェクトを引数として `dayOfYear()` を呼び出します。

```js
dayOfYear(new Date()); // 272
```
