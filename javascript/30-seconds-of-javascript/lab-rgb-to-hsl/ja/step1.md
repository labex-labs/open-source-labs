# RGB から HSL への変換

RGB カラー タプルを HSL 形式に変換するには、次の手順に従います。

1. コーディングの練習を始めるために、ターミナル/SSH を開きます。
2. `node` と入力し、Enter キーを押します。
3. [RGB から HSL の変換式](https://www.niwa.nu/2013/05/math-behind-colorspace-conversions-rgb-hsl/)を使用して、適切な形式に変換します。
4. すべての入力パラメータが [0, 255] の範囲内に収まることを確認します。
5. 得られる値は、H: [0, 360]、S: [0, 100]、L: [0, 100] の範囲内に収まる必要があります。

次に、JavaScript の RGBToHSL 関数の例を示します。

```js
const RGBToHSL = (r, g, b) => {
  r /= 255;
  g /= 255;
  b /= 255;
  const l = Math.max(r, g, b);
  const s = l - Math.min(r, g, b);
  const h = s
    ? l === r
      ? (g - b) / s
      : l === g
        ? 2 + (b - r) / s
        : 4 + (r - g) / s
    : 0;
  return [
    60 * h < 0 ? 60 * h + 360 : 60 * h,
    100 * (s ? (l <= 0.5 ? s / (2 * l - s) : s / (2 - (2 * l - s))) : 0),
    (100 * (2 * l - s)) / 2
  ];
};
```

RGBToHSL 関数の使用例を次に示します。

```js
RGBToHSL(45, 23, 11); // [21.17647, 60.71428, 10.98039]
```
