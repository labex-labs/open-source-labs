# JavaScript を使って HSL を RGB に変換する

HSL 形式のカラー タプルを RGB に変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. [HSL から RGB への変換公式](https://en.wikipedia.org/wiki/HSL_and_HSV#HSL_to_RGB)を使用して、カラー タプルを適切な形式に変換します。
3. 入力パラメータが次の範囲内であることを確認します。H: [0, 360]、S: [0, 100]、L: [0, 100]。
4. 出力値は [0, 255] の範囲内にする必要があります。

以下は、HSL から RGB への変換公式の JavaScript コードです。

```js
const HSLToRGB = (h, s, l) => {
  s /= 100;
  l /= 100;
  const k = (n) => (n + h / 30) % 12;
  const a = s * Math.min(l, 1 - l);
  const f = (n) =>
    l - a * Math.max(-1, Math.min(k(n) - 3, Math.min(9 - k(n), 1)));
  return [255 * f(0), 255 * f(8), 255 * f(4)];
};
```

この関数を使用するには、引数として H、S、および L の値を指定します。

```js
HSLToRGB(13, 100, 11); // [56.1, 12.155, 0]
```
