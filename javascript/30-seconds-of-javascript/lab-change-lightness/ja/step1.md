# HSL カラーの明度を変更する方法

`hsl()` カラー文字列の明度値を変更するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。

2. `String.prototype.match()` を使用して、`hsl()` 文字列から数値を持つ 3 つの文字列を含む配列を取得します。

3. `Array.prototype.map()` を `Number` と組み合わせて使用して、文字列を数値の配列に変換します。

4. `Math.max()` と `Math.min()` を使用して、明度値が有効な範囲（`0` から `100` の間）に収まることを確認します。

5. テンプレートリテラルを使用して、更新された明度値を持つ新しい `hsl()` 文字列を作成します。

これらの手順を実装するコードの例を次に示します。

```js
const changeLightness = (delta, hslStr) => {
  const [hue, saturation, lightness] = hslStr.match(/\d+/g).map(Number);

  const newLightness = Math.max(
    0,
    Math.min(100, lightness + parseFloat(delta))
  );

  return `hsl(${hue}, ${saturation}%, ${newLightness}%)`;
};
```

その後、デルタ値と `hsl()` 文字列を渡して `changeLightness()` 関数を呼び出すことで、更新された明度値を持つ新しい `hsl()` 文字列を取得できます。たとえば：

```js
changeLightness(10, "hsl(330, 50%, 50%)"); // 'hsl(330, 50%, 60%)'
changeLightness(-10, "hsl(330, 50%, 50%)"); // 'hsl(330, 50%, 40%)'
```
