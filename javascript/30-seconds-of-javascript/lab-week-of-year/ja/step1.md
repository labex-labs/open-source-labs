# JavaScript で日付から年の週を取得する

JavaScript で日付に対応する 0 から始まる年の週を取得するには、以下の手順に従ってください。

1. `date` パラメータを受け取る `weekOfYear` 関数を作成します。
2. `Date` コンストラクタと `Date.prototype.getFullYear()` を使用して、その年の最初の日を `Date` オブジェクトとして取得します。
3. `Date.prototype.setDate()`、`Date.prototype.getDate()`、`Date.prototype.getDay()` と剰余演算子 (`%`) を使用して、その年の最初の月曜日を取得します。
4. 指定された `date` からその年の最初の月曜日を引き、1 週間のミリ秒数で割ります。
5. `Math.round()` を使用して、指定された `date` に対応する 0 から始まる年の週を取得します。
6. 指定された `date` がその年の最初の月曜日より前の場合、`-0` が返されます。

コードは次のとおりです。

```js
const weekOfYear = (date) => {
  const startOfYear = new Date(date.getFullYear(), 0, 1);
  startOfYear.setDate(startOfYear.getDate() + (startOfYear.getDay() % 7));
  return Math.round((date - startOfYear) / (7 * 24 * 3600 * 1000));
};
```

`weekOfYear` 関数を使用するには、`Date` オブジェクトをパラメータとして渡して呼び出すだけです。

```js
weekOfYear(new Date("2021-06-18")); // 23
```

これにより、指定された日付に対応する 0 から始まる年の週が返されます。この場合は `23` です。
