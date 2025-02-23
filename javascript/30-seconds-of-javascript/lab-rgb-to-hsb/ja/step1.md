# RGB から HSB への変換

RGB カラー タプルを HSB 形式に変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. [RGB から HSB の変換式](https://en.wikipedia.org/wiki/HSL_and_HSV#From_RGB) を使用して、RGB カラー タプルを適切な HSB 形式に変換します。
3. 入力パラメータの範囲は [0, 255] ですが、結果の値の範囲は次のとおりです。

- H: [0, 360]
- S: [0, 100]
- B: [0, 100]

次に、JavaScript の関数です。

```js
const RGBToHSB = (r, g, b) => {
  r /= 255;
  g /= 255;
  b /= 255;
  const v = Math.max(r, g, b),
    n = v - Math.min(r, g, b);
  const h =
    n === 0
      ? 0
      : n && v === r
        ? (g - b) / n
        : v === g
          ? 2 + (b - r) / n
          : 4 + (r - g) / n;
  return [60 * (h < 0 ? h + 6 : h), v && (n / v) * 100, v * 100];
};
```

この関数を次のように呼び出すことができます。

```js
RGBToHSB(252, 111, 48);
// [18.529411764705856, 80.95238095238095, 98.82352941176471]
```
