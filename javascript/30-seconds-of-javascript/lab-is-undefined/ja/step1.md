# 未定義値のチェック

値が未定義であるかどうかを確認するには、ターミナル/SSH を開き、`node` と入力します。

- 厳密な等値演算子を使用して、`val` が `undefined` と等しいかどうかを確認します。

```js
const isUndefined = (val) => val === undefined;
```

```js
isUndefined(undefined); // true
```

このコードは、指定された値が未定義であるかどうかを確認します。
