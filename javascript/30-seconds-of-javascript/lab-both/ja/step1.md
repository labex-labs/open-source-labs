# 関数と論理 AND の使用

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。

与えられた一連の引数に対して 2 つの関数が `true` を返すかどうかを確認するには、論理 AND (`&&`) 演算子を使用します。

```js
const both =
  (f, g) =>
  (...args) =>
    f(...args) && g(...args);
```

上記のコードは、2 つの関数 `f` と `g` を入力として受け取り、与えられた引数で `f` と `g` を呼び出し、両方の関数が `true` を返す場合にのみ `true` を返す別の関数を返す、新しい関数 `both` を作成します。

たとえば、数値が正で偶数であるかどうかを確認するには、次のように `isEven` と `isPositive` 関数を `both` とともに使用できます。

```js
const isEven = (num) => num % 2 === 0;
const isPositive = (num) => num > 0;
const isPositiveEven = both(isEven, isPositive);
isPositiveEven(4); // true
isPositiveEven(-2); // false
```

ここで、`isPositiveEven` は、入力として `isEven` と `isPositive` を使用して `both` 関数を使って、与えられた数値が正で偶数であるかどうかを確認する新しい関数です。
