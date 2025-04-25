# 整数をローマ数字に変換する

整数をローマ数字表記に変換するには、以下の手順に従ってください。

1. ターミナル/SSH を開き、`node` と入力してコーディングの練習を開始します。

2. `toRomanNumeral()` 関数は、`1` から `3999` までの値（両端を含む）を受け付けます。

3. (ローマ数字の値，整数) の形式の 2 値配列を含むルックアップテーブルを作成します。

4. `Array.prototype.reduce()` を使用して、`lookup` 内の値をループし、`num` をその値で繰り返し割ります。

5. `String.prototype.repeat()` を使用して、ローマ数字表記をアキュムレータに追加します。

以下は `toRomanNumeral()` 関数のコードです。

```js
const toRomanNumeral = (num) => {
  const lookup = [
    ["M", 1000],
    ["CM", 900],
    ["D", 500],
    ["CD", 400],
    ["C", 100],
    ["XC", 90],
    ["L", 50],
    ["XL", 40],
    ["X", 10],
    ["IX", 9],
    ["V", 5],
    ["IV", 4],
    ["I", 1]
  ];
  return lookup.reduce((acc, [k, v]) => {
    acc += k.repeat(Math.floor(num / v));
    num = num % v;
    return acc;
  }, "");
};
```

以下の例で関数をテストすることができます。

```js
toRomanNumeral(3); // 'III'
toRomanNumeral(11); // 'XI'
toRomanNumeral(1998); // 'MCMXCVIII'
```
