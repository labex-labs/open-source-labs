# JavaScriptで数値を指定された精度に丸める方法

```
const round = (n, decimals = 0) =>
  Number(`${Math.round(`${n}e${decimals}`)}e-${decimals}`);
```

- `Math.round()` とテンプレートリテラルを使って、数値を指定された桁数に丸めます。
- 整数に丸めたい場合は、2番目の引数 `decimals` を省略します。
- コーディングの練習を始めるには、ターミナル/SSHを開いて `node` と入力します。
- たとえば、`round(1.005, 2)` を実行すると `1.01` が返されます。
