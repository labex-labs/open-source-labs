# ユークリッド距離の計算

任意の次元数の 2 点間の距離を計算するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために`node`と入力します。
2. `Object.keys()`と`Array.prototype.map()`を使って、各座標を 2 点間の差分にマッピングします。
3. `Math.hypot()`を使って、2 点間のユークリッド距離を計算します。

始めるのに役立つサンプルコードの断片を以下に示します。

```js
const euclideanDistance = (a, b) =>
  Math.hypot(...Object.keys(a).map((k) => b[k] - a[k]));
```

これらのサンプル入力を使って関数を試すことができます。

```js
euclideanDistance([1, 1], [2, 3]); // ~2.2361
euclideanDistance([1, 1, 1], [2, 3, 2]); // ~2.4495
```
