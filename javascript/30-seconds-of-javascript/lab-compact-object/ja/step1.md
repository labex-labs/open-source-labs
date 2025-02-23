# コンパクトなオブジェクトアルゴリズム

オブジェクトまたは配列からすべての偽値を深く削除するには、次のアルゴリズムを使用します。

1. 再帰を使用して、各ネストされたオブジェクトまたは配列に対して `compactObject()` 関数を呼び出します。
2. `Array.isArray()`、`Array.prototype.filter()`、および `Boolean()` を使用して反復可能なデータを初期化します。これは、疎な配列を避けるために行われます。
3. `Object.keys()` と `Array.prototype.reduce()` を使用して、適切な初期値で各キーを反復処理します。
4. `Boolean()` を使用して各キーの値の真偽性を判断し、真の場合にはそれをアキュムレータに追加します。
5. `typeof` を使用して、与えられた値が `object` であるかどうかを判断し、それを再帰的にコンパクト化するために関数を再度呼び出します。

以下は、`compactObject()` 関数のコードです。

```js
const compactObject = (val) => {
  const data = Array.isArray(val) ? val.filter(Boolean) : val;
  return Object.keys(data).reduce(
    (acc, key) => {
      const value = data[key];
      if (Boolean(value))
        acc[key] = typeof value === "object" ? compactObject(value) : value;
      return acc;
    },
    Array.isArray(val) ? [] : {}
  );
};
```

この関数を使用するには、オブジェクトまたは配列を引数として `compactObject()` に渡します。関数は、すべての偽値が削除された新しいオブジェクトまたは配列を返します。

たとえば：

```js
const obj = {
  a: null,
  b: false,
  c: true,
  d: 0,
  e: 1,
  f: "",
  g: "a",
  h: [null, false, "", true, 1, "a"],
  i: { j: 0, k: false, l: "a" }
};
compactObject(obj);
// { c: true, e: 1, g: 'a', h: [ true, 1, 'a' ], i: { l: 'a' } }
```
