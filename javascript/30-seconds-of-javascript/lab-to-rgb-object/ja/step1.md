# RGB をオブジェクトに変換する

`rgb()` カラー文字列を各色の値を持つオブジェクトに変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `String.prototype.match()` を使用して、数値を含む 3 つの文字列を要素とする配列を取得します。
3. `Array.prototype.map()` を `Number` と組み合わせて使用して、それらを数値の配列に変換します。
4. 配列の分解構文を使用して、値を名前付きの変数に格納し、それらから適切なオブジェクトを作成します。

使用できるコードは次のとおりです。

```js
const toRGBObject = (rgbStr) => {
  const [red, green, blue] = rgbStr.match(/\d+/g).map(Number);
  return { red, green, blue };
};

toRGBObject("rgb(255, 12, 0)"); // {red: 255, green: 12, blue: 0}
```
