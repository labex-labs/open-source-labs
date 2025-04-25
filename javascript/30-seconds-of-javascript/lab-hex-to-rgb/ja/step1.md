# 16 進数から RGB への変換

16 進数の色コード（`#`接頭辞付きまたはなし）を RGB 文字列に変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために`node`と入力します。
2. ビット右シフト演算子を使用し、`&`（論理積）演算子でビットをマスクします。
3. 色コードが 3 桁の場合、まず 6 桁のバージョンに変換します。
4. 6 桁の 16 進数にアルファ値が付けられている場合、`rgba()`文字列を返します。

以下は変換用の JavaScript コードです。

```js
const hexToRGB = (hex) => {
  let alpha = false,
    h = hex.slice(hex.startsWith("#") ? 1 : 0);
  if (h.length === 3) h = [...h].map((x) => x + x).join("");
  else if (h.length === 8) alpha = true;
  h = parseInt(h, 16);
  return (
    "rgb" +
    (alpha ? "a" : "") +
    "(" +
    (h >>> (alpha ? 24 : 16)) +
    ", " +
    ((h & (alpha ? 0x00ff0000 : 0x00ff00)) >>> (alpha ? 16 : 8)) +
    ", " +
    ((h & (alpha ? 0x0000ff00 : 0x0000ff)) >>> (alpha ? 8 : 0)) +
    (alpha ? `, ${h & 0x000000ff}` : "") +
    ")"
  );
};
```

次の例で`hexToRGB`関数を使用できます。

```js
hexToRGB("#27ae60ff"); // 'rgba(39, 174, 96, 255)'
hexToRGB("27ae60"); // 'rgb(39, 174, 96)'
hexToRGB("#fff"); // 'rgb(255, 255, 255)'
```
