# 値がオブジェクトのようなものかどうかを確認する

値がオブジェクトのようなものかどうかを確認するには、次の手順に従います。

1. ターミナル/SSH を開きます。
2. コーディングの練習を始めるために `node` を入力します。
3. 提供された値が `null` でなく、その `typeof` が `'object'` に等しいかどうかを確認します。

使用できるコードは次のとおりです。

```js
const isObjectLike = (val) => val !== null && typeof val === "object";
```

この関数を次の例でテストできます。

```js
isObjectLike({}); // true
isObjectLike([1, 2, 3]); // true
isObjectLike((x) => x); // false
isObjectLike(null); // false
```
