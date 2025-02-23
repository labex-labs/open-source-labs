# Box-Muller 変換を使ったガウス乱数の生成

Box-Muller 変換を使ってガウス（正規分布）乱数を生成するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. Box-Muller 変換を利用してガウス分布を持つ乱数を生成するための提供されたコード スニペットを使用します。
3. コード スニペットに提供されている `randomGauss()` 関数は、ガウス分布を持つ乱数を生成します。
4. `randomGauss()` 関数の出力は 0 から 1 の間の数です。
5. 出力は、統計シミュレーション、データ分析、機械学習など、さまざまなアプリケーションで使用できます。

```js
const randomGauss = () => {
  const theta = 2 * Math.PI * Math.random();
  const rho = Math.sqrt(-2 * Math.log(1 - Math.random()));
  return (rho * Math.cos(theta)) / 10.0 + 0.5;
};
```

使用例：

```js
randomGauss(); // 0.5
```
