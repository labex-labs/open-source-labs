# 範囲内で数値をクランプする関数

指定された範囲内で数値をクランプするには、`clampNumber` 関数を使用します。

まず、ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。

`clampNumber` 関数には 3 つのパラメータがあります。`num`、`a`、および `b`。この関数は、境界値 `a` と `b` によって指定された包含範囲内で `num` をクランプし、結果を返します。

`num` が範囲内にある場合、関数は `num` を返します。それ以外の場合は、範囲内の最も近い数値を返します。

ここに `clampNumber` 関数のコードを示します。

```js
const clampNumber = (num, a, b) =>
  Math.max(Math.min(num, Math.max(a, b)), Math.min(a, b));
```

この関数の使い方の例をいくつか示します。

```js
clampNumber(2, 3, 5); // 3
clampNumber(1, -1, -5); // -1
```
