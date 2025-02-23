# HSL からオブジェクトへの変換

`hsl()` カラー文字列を各カラーの数値を持つオブジェクトに変換するには、次の手順に従います。

- ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
- `String.prototype.match()` を使用して、数値を含む 3 つの文字列を持つ配列を取得します。
- `Array.prototype.map()` と `Number` を組み合わせて、文字列を数値の配列に変換します。
- 配列の分解構文を使用して、値を名前付きの変数に格納します。
- 名前付きの変数から適切なオブジェクトを作成します。

```js
const toHSLObject = (hslStr) => {
  const [hue, saturation, lightness] = hslStr.match(/\d+/g).map(Number);
  return { hue, saturation, lightness };
};
```

使用例:

```js
toHSLObject("hsl(50, 10%, 10%)"); // { hue: 50, saturation: 10, lightness: 10 }
```
