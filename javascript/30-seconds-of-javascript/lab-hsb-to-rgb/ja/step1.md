# HSBからRGBへの変換

HSBカラータプルをRGB形式に変換するには、次の手順に従います。

- ターミナル/SSHを開き、コーディングの練習を始めるために `node` と入力します。
- [HSBからRGBへの変換式](https://en.wikipedia.org/wiki/HSL_and_HSV#HSV_to_RGB) を使用して適切な形式に変換します。
- 入力パラメータは、H: [0, 360]、S: [0, 100]、B: [0, 100] の範囲にする必要があります。
- すべての出力値は、[0, 255] の範囲にする必要があります。

以下は、HSBをRGBに変換するために使用できるコードです。

```js
const HSBToRGB = (h, s, b) => {
  s /= 100;
  b /= 100;
  const k = (n) => (n + h / 60) % 6;
  const f = (n) => b * (1 - s * Math.max(0, Math.min(k(n), 4 - k(n), 1)));
  return [255 * f(5), 255 * f(3), 255 * f(1)];
};
```

たとえば、HSBカラータプル (18, 81, 99) をRGB形式に変換したい場合は、次のコードを使用できます。

```js
HSBToRGB(18, 81, 99); // [252.45, 109.31084999999996, 47.965499999999984]
```
