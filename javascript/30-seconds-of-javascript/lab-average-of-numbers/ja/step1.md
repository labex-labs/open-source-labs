# JavaScript で数値の平均を計算する方法

JavaScript で 2 つ以上の数値の平均を計算するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. 組み込みの `Array.prototype.reduce()` メソッドを使用して、各値を `0` の値で初期化されたアキュムレータに追加します。
3. 得られた合計を配列の長さで割ります。

使用できるサンプル コード スニペットは次のとおりです。

```js
const average = (...nums) =>
  nums.reduce((acc, val) => acc + val, 0) / nums.length;
```

`average` 関数を配列または複数の引数で呼び出すことができます。

```js
average(...[1, 2, 3]); // 2
average(1, 2, 3); // 2
```
