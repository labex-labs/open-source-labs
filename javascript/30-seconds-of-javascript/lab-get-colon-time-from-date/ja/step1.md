# 日付オブジェクトからコロン付きの時間を取得する方法

コーディングの練習をしたい場合は、まずターミナル/SSH を開いて `node` と入力することから始めることができます。

この関数は、与えられた `Date` オブジェクトから `HH:MM:SS` 形式の文字列を返します。

これを達成するために、`Date.prototype.toTimeString()` と `String.prototype.slice()` メソッドを利用して、`Date` オブジェクトの `HH:MM:SS` 部分を抽出します。

ここに関数のコードを示します。

```js
const getColonTimeFromDate = (date) => date.toTimeString().slice(0, 8);
```

そして、使用例を以下に示します。

```js
getColonTimeFromDate(new Date()); // '08:38:00'
```
