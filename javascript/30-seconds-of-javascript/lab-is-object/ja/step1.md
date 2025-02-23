# 値がオブジェクトであるかどうかを判断する

渡された値がオブジェクトであるかどうかを判断するには、ターミナル/SSH を開いて `node` と入力します。以下の手順が行われます。

- `Object` コンストラクタは、与えられた値に対するオブジェクト ラッパーを作成します。
- 値が `null` または `undefined` の場合、空のオブジェクトが作成されて返されます。
- 値が `null` または `undefined` でない場合、与えられた値に対応する型のオブジェクトが返されます。

以下は、値がオブジェクトであるかどうかを確認する関数の例です。

```js
const isObject = (obj) => obj === Object(obj);
```

`isObject` 関数を使用するいくつかの例を以下に示します。

```js
isObject([1, 2, 3, 4]); // true
isObject([]); // true
isObject(["Hello!"]); // true
isObject({ a: 1 }); // true
isObject({}); // true
isObject(true); // false
```
