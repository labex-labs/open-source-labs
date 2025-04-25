# キーの配列を使ってオブジェクト内のネストされた値を取得する方法

ネストされた JSON オブジェクトから特定の値を取得するには、`deepGet` 関数を使用できます。この関数はオブジェクトとキーの配列を受け取り、オブジェクト内に存在する場合にはターゲット値を返します。

`deepGet` 関数を使用するには：

- ネストされた JSON オブジェクトから取得したいキーの配列を作成します。
- オブジェクトとキーの配列を使って `deepGet` 関数を呼び出します。
- 関数は存在する場合にはターゲット値を返し、存在しない場合には `null` を返します。

以下は `deepGet` 関数のコードです：

```js
const deepGet = (obj, keys) =>
  keys.reduce(
    (xs, x) => (xs && xs[x] !== null && xs[x] !== undefined ? xs[x] : null),
    obj
  );
```

以下は `deepGet` 関数の使い方の例です：

```js
let index = 2;
const data = {
  foo: {
    foz: [1, 2, 3],
    bar: {
      baz: ["a", "b", "c"]
    }
  }
};
deepGet(data, ["foo", "foz", index]); // 3 を返す
deepGet(data, ["foo", "bar", "baz", 8, "foz"]); // null を返す
```

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。
