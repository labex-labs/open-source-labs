# 日付オブジェクトから曜日名を取得する

`Date` オブジェクトから曜日名を取得するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `Date.prototype.toLocaleDateString()` に `{ weekday: 'long' }` オプションを使って曜日を取得します。
3. 任意の 2 番目の引数を使って言語固有の名前を取得することもできますし、それを省略して既定のロケールを使うこともできます。

以下はサンプルの実装です。

```js
const dayName = (date, locale) =>
  date.toLocaleDateString(locale, { weekday: "long" });
```

この関数を次のように使うことができます。

```js
dayName(new Date()); // 'Saturday'
dayName(new Date("09/23/2020"), "de-DE"); // 'Samstag'
```
