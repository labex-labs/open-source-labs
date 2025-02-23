# 条件に一致する最後のキーを見つける関数

与えられた条件を満たすオブジェクトの最後のキーを見つけるには、`findLastKey` 関数を使用します。この関数は、オブジェクトとテスト関数を引数として取ります。一致するキーが見つかると、そのキーを返します。そうでなければ、`undefined` を返します。この関数が最後のキーを見つけるためにとる手順は次のとおりです。

1. `Object.keys()` を使用して、オブジェクトのすべてのプロパティを取得します。
2. `Array.prototype.reverse()` を使用して、キーの順序を逆にします。
3. `Array.prototype.find()` を使用して、各キーと値のペアに対して提供された関数をテストします。コールバック関数には、値、キー、オブジェクトの3つの引数が渡されます。
4. 一致するキーが見つかったら、それを返します。

```js
const findLastKey = (obj, fn) =>
  Object.keys(obj)
    .reverse()
    .find((key) => fn(obj[key], key, obj));
```

`findLastKey` を使用する例を次に示します。

```js
findLastKey(
  {
    barney: { age: 36, active: true },
    fred: { age: 40, active: false },
    pebbles: { age: 1, active: true }
  },
  (x) => x["active"]
); // 'pebbles'
```

この関数を使用するには、ターミナル/SSHを開き、コーディングを練習するために `node` と入力します。
