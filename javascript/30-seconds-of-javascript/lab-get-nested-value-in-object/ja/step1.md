# JSON オブジェクトのネストされた値を取得する方法

与えられたキーに基づいてネストされた JSON オブジェクトからターゲット値を取得するには、次の手順に従います。

- ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
- `in` 演算子を使用して、`obj` に `target` が存在するかどうかを確認します。
- `target` が見つかった場合、`obj` の対応する値を返します。
- `target` が見つからなかった場合、`Object.values()` と `Array.prototype.reduce()` を使用して、最初の一致するキー/値のペアが見つかるまで、各ネストされたオブジェクトに対して再帰的に `dig` 関数を呼び出します。

以下は、`dig` 関数のコードです。

```js
const dig = (obj, target) =>
  target in obj
    ? obj[target]
    : Object.values(obj).reduce((acc, val) => {
        if (acc !== undefined) return acc;
        if (typeof val === "object") return dig(val, target);
      }, undefined);
```

`dig` 関数を使用するには、まず次のようにネストされた階層を持つ JSON オブジェクトを作成します。

```js
const data = {
  level1: {
    level2: {
      level3: "some data"
    }
  }
};
```

次に、JSON オブジェクトと必要なキーを使って `dig` 関数を呼び出します。

```js
dig(data, "level3"); //'some data'
dig(data, "level4"); // undefined
```

これらの例では、`data` オブジェクトの `level3` キーの値が返され、存在しない `level4` キーに対しては `undefined` が返されます。
