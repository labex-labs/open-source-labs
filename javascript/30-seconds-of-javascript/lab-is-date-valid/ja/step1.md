# 日付が有効かどうかを確認する方法

日付が有効かどうかを確認するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. スプレッド演算子 (`...`) を使用して、引数の配列を `Date` コンストラクタに渡します。
3. `Date.prototype.valueOf()` と `Number.isNaN()` を使用して、与えられた値から有効な `Date` オブジェクトを作成できるかどうかを確認します。

以下はコードの例です。

```js
const isDateValid = (...val) => !Number.isNaN(new Date(...val).valueOf());
```

次のように、異なる値で関数をテストできます。

```js
isDateValid("December 17, 1995 03:24:00"); // true
isDateValid("1995-12-17T03:24:00"); // true
isDateValid("1995-12-17 T03:24:00"); // false
isDateValid("Duck"); // false
isDateValid(1995, 11, 17); // true
isDateValid(1995, 11, 17, "Duck"); // false
isDateValid({}); // false
```
