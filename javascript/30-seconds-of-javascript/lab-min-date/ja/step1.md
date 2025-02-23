# JavaScript で最小日付を見つける方法

JavaScript で最小日付値を見つけるには、ES6 のスプレッド構文を `Math.min()` と `Date` コンストラクタとともに使用できます。以下はコードのサンプルです。

```js
const minDate = (...dates) => new Date(Math.min(...dates));
```

この関数を使用するには、`Date` オブジェクトの配列を作成し、スプレッド構文を使って `minDate()` に渡します。以下は例です。

```js
const dates = [
  new Date(2017, 4, 13),
  new Date(2018, 2, 12),
  new Date(2016, 0, 10),
  new Date(2016, 0, 9)
];
minDate(...dates); // 2016-01-08T22:00:00.000Z を表す `Date` オブジェクトを返す
```

このコードを使用することで、JavaScript で最小日付値を簡単に見つけることができます。
