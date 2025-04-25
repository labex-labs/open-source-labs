# 値が単純なオブジェクトかどうかを確認する

値が単純なオブジェクトかどうかを確認するには、次の手順に従います。

- 値が真であることを確認する。
- `typeof`を使用して、それがオブジェクトであることを確認する。
- `Object.prototype.constructor`を使用して、コンストラクタが`Object`に等しいことを確認する。

このチェックを実装するには、次のコードを使用します。

```js
const isPlainObject = (val) =>
  !!val && typeof val === "object" && val.constructor === Object;
```

次の例でこの関数をテストできます。

```js
isPlainObject({ a: 1 }); // true
isPlainObject(new Map()); // false
```

コーディングの練習を始めるには、ターミナル/SSH を開いて`node`と入力します。
