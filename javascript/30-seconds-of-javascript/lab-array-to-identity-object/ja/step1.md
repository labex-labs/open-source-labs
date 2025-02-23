# 配列を ID オブジェクトに変換する方法

コーディングを練習したい場合は、ターミナル/SSH を開いて `node` と入力します。値の配列をキーと値が同じオブジェクトに変換するには、次の手順に従います。

1. `Array.prototype.map()` を使って各値をキーと値のペアの配列にマッピングします。
2. `Object.fromEntries()` を使ってキーと値のペアの配列をオブジェクトに変換します。

コードは次のとおりです。

```js
const toIdentityObject = (arr) => Object.fromEntries(arr.map((v) => [v, v]));
```

そして、例は次のとおりです。

```js
toIdentityObject(["a", "b"]); // { a: 'a', b: 'b' }
```
