# ベクトル距離の計算

2 つのベクトル間の距離を計算するには、次の手順に従います。

1. コーディングの練習を始めるために、ターミナル/SSH を開きます。
2. コードを始めるには `node` と入力します。
3. `Array.prototype.reduce()`、`Math.pow()`、および `Math.sqrt()` を使用して、ベクトル間のユークリッド距離を求めます。
4. 以下に示す `vectorDistance` 式を適用します。

```js
const vectorDistance = (x, y) =>
  Math.sqrt(x.reduce((acc, val, i) => acc + Math.pow(val - y[i], 2), 0));
```

5. 次の形式で 2 つのベクトルを入力して式をテストします。`vectorDistance([10, 0, 5], [20, 0, 10]);`
6. 出力は 2 つのベクトル間の距離になります。`11.180339887498949`。
