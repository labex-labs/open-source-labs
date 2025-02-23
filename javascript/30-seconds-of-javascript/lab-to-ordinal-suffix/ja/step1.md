# 数値を順序接尾辞に変換する関数

数値を順序接尾辞に変換するには、`toOrdinalSuffix`関数を使用します。

- ターミナル/SSHを開き、コーディングの練習を始めるには`node`と入力します。
- この関数は数値を入力として受け取り、正しい順序指示子接尾辞付きの文字列として返します。
- 剰余演算子（`%`）を使用して、単一桁と十の位の値を見つけます。
- どの順序パターンの桁が一致するかを見つけます。
- 桁が10代のパターンに見つかった場合は、10代の順序を使用します。

```js
const toOrdinalSuffix = (num) => {
  const int = parseInt(num),
    digits = [int % 10, int % 100],
    ordinals = ["st", "nd", "rd", "th"],
    oPattern = [1, 2, 3, 4],
    tPattern = [11, 12, 13, 14, 15, 16, 17, 18, 19];
  return oPattern.includes(digits[0]) && !tPattern.includes(digits[1])
    ? int + ordinals[digits[0] - 1]
    : int + ordinals[3];
};
```

ここでは、`toOrdinalSuffix`関数を使用する例を示します。

```js
toOrdinalSuffix("123"); // '123rd'
```
