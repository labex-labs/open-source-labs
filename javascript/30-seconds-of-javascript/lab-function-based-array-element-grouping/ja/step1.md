# 配列要素をグループ化する方法

コーディングを練習したい場合は、ターミナル/SSHを開いて `node` を入力することから始めることができます。準備ができたら、次の手順を使って、与えられた関数に基づいて配列の要素をグループ化することができます。

1. `Array.prototype.map()` を使って、配列の値を関数またはプロパティ名にマッピングします。
2. `Array.prototype.reduce()` を使って、キーがマッピング結果から生成されるオブジェクトを作成します。

以下はコードの例です。

```js
const groupBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val, i) => {
      acc[val] = (acc[val] || []).concat(arr[i]);
      return acc;
    }, {});
```

コードをテストするには、次の例を使うことができます。

```js
groupBy([6.1, 4.2, 6.3], Math.floor); // {4: [4.2], 6: [6.1, 6.3]}
groupBy(["one", "two", "three"], "length"); // {3: ['one', 'two'], 5: ['three']}
```

これらは、指定された関数に基づくキーと、関数に一致する元の要素の配列である値を持つオブジェクトを返します。
