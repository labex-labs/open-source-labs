# 配列の差分

2 つの配列の差分を見つけるには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを開始するために `node` と入力します。

2. 配列 `b` から `Set` を作成して、`b` から一意の値を抽出します。

3. `Set.prototype.has()` を使用して、配列 `a` で `Array.prototype.filter()` を使用して、配列 `b` に含まれていない値のみを残します。

以下がコードです。

```js
const difference = (a, b) => {
  const s = new Set(b);
  return a.filter((x) => !s.has(x));
};
```

使用例：

```js
difference([1, 2, 3, 3], [1, 2, 4]); // 出力：[3, 3]
```
