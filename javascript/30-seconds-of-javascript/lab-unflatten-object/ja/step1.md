# JavaScript でオブジェクトを展開する方法

JavaScript でキーにパスがあるオブジェクトを展開するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。

2. ネストされた `Array.prototype.reduce()` を使って、フラットなパスをリーフノードに変換します。

3. `String.prototype.split()` を使って各キーをドット区切り文字で分割し、`Array.prototype.reduce()` を使ってキーに対してオブジェクトを追加します。

4. 現在のアキュムレータに既に特定のキーに対応する値が含まれている場合、その値を次のアキュムレータとして返します。

5. それ以外の場合、適切なキーと値のペアをアキュムレータオブジェクトに追加し、値をアキュムレータとして返します。

ここに `unflattenObject` 関数のコードがあります。

```js
const unflattenObject = (obj) =>
  Object.keys(obj).reduce((res, k) => {
    k.split(".").reduce(
      (acc, e, i, keys) =>
        acc[e] ||
        (acc[e] = isNaN(Number(keys[i + 1]))
          ? keys.length - 1 === i
            ? obj[k]
            : {}
          : []),
      res
    );
    return res;
  }, {});
```

JavaScript でオブジェクトを展開するために `unflattenObject` 関数を使用できます。

```js
unflattenObject({ "a.b.c": 1, d: 1 }); // { a: { b: { c: 1 } }, d: 1 }
unflattenObject({ "a.b": 1, "a.c": 2, d: 3 }); // { a: { b: 1, c: 2 }, d: 3 }
unflattenObject({ "a.b.0": 8, d: 3 }); // { a: { b: [ 8 ] }, d: 3 }
```
