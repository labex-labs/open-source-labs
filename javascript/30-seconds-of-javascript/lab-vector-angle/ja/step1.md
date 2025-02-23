# ベクトルの角度の計算

2 つのベクトルの間の角度（θ）を計算するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `Array.prototype.reduce()`、`Math.pow()`、および `Math.sqrt()` を使用して、各ベクトルの大きさと 2 つのベクトルのスカラー積を計算します。
3. `Math.acos()` を使用して逆余弦を計算し、θ の値を取得します。

以下はコードの例です。

```js
const vectorAngle = (x, y) => {
  let mX = Math.sqrt(x.reduce((acc, n) => acc + Math.pow(n, 2), 0));
  let mY = Math.sqrt(y.reduce((acc, n) => acc + Math.pow(n, 2), 0));
  return Math.acos(x.reduce((acc, n, i) => acc + n * y[i], 0) / (mX * mY));
};

vectorAngle([3, 4], [4, 3]); // 0.283794109208328
```

この関数は 2 つの配列（`x` と `y`）を引数として受け取り、それらの間の角度（ラジアン）を返します。
