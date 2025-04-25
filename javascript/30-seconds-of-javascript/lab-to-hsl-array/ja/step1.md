# HSL を配列に変換する

`hsl()`カラー文字列を値の配列に変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために`node`と入力します。
2. `String.prototype.match()`を使って、数値を含む 3 つの文字列を要素とする配列を取得します。
3. `Array.prototype.map()`を`Number`と組み合わせて、それらを数値の配列に変換します。

以下は、`hsl()`カラー文字列を数値の配列に変換するコードです。

```js
const toHSLArray = (hslStr) => hslStr.match(/\d+/g).map(Number);
```

使用例：

```js
toHSLArray("hsl(50, 10%, 10%)"); // [50, 10, 10]
```
