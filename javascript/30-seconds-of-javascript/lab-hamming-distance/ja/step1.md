# ハミング距離の計算

2 つの値間のハミング距離を計算するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. 排他的論理和（XOR）演算子 (`^`) を使用して、2 つの数値間のビットの違いを見つけます。
3. `Number.prototype.toString()` を使用して、結果を 2 進数文字列に変換します。
4. `String.prototype.match()` を使用して、文字列中の `1` の数を数えます。
5. その数を返します。

以下は、`hammingDistance` 関数のコードです。

```js
const hammingDistance = (num1, num2) =>
  ((num1 ^ num2).toString(2).match(/1/g) || "").length;
```

`hammingDistance(2, 3); // 1` を実行することで、この関数をテストできます。
