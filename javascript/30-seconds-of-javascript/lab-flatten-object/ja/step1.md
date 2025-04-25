# オブジェクトのフラット化

キーのパス付きでオブジェクトをフラット化するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. 再帰を使ってオブジェクトをフラット化します。
3. `Object.keys()` を `Array.prototype.reduce()` と組み合わせて、すべてのリーフノードをフラット化されたパスノードに変換します。
4. キーの値がオブジェクトの場合、`Object.assign()` を使ってパスを作成するために適切な `prefix` で関数を再帰的に呼び出します。
5. それ以外の場合、適切な接頭辞付きのキーバリューペアをアキュムレータオブジェクトに追加します。
6. すべてのキーに接頭辞を付けたい場合を除き、2 番目の引数 `prefix` を省略します。

以下はサンプルの実装です。

```js
const flattenObject = (obj, prefix = "") =>
  Object.keys(obj).reduce((acc, k) => {
    const pre = prefix.length ? `${prefix}.` : "";
    if (
      typeof obj[k] === "object" &&
      obj[k] !== null &&
      Object.keys(obj[k]).length > 0
    ) {
      Object.assign(acc, flattenObject(obj[k], pre + k));
    } else {
      acc[pre + k] = obj[k];
    }
    return acc;
  }, {});
```

この `flattenObject` 関数を次のように使うことができます。

```js
flattenObject({ a: { b: { c: 1 } }, d: 1 }); // { 'a.b.c': 1, d: 1 }
```
