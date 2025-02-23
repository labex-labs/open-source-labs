# JavaScript で日付から Unix タイムスタンプを取得する方法

コーディングを始めるには、ターミナル/SSH を開いて `node` と入力します。

JavaScript の `Date` オブジェクトから Unix タイムスタンプを取得するには、次の手順を使用できます。

1. `Date.prototype.getTime()` を使用してミリ秒単位のタイムスタンプを取得します。
2. タイムスタンプを `1000` で割って秒単位のタイムスタンプを取得します。
3. `Math.floor()` を使用して結果のタイムスタンプを整数に丸めます。
4. `date` 引数を省略すると、現在の日付が使用されます。

以下はコードの例です。

```js
const getTimestamp = (date = new Date()) => Math.floor(date.getTime() / 1000);
```

`getTimestamp()` 関数を呼び出して Unix タイムスタンプを取得できます。たとえば：

```js
getTimestamp(); // 1602162242
```
