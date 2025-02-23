# 関数に対する論理和の使用

コーディングの練習を始めるには、ターミナル/SSHを開いて `node` と入力します。

論理和 (`||`) 演算子を使って、与えられた引数セットに対して少なくとも1つの関数が `true` を返すかどうかを確認できます。これを行うには、提供された `引数` で2つの関数を呼び出し、それらの結果に論理和演算子を適用します。

以下は、`either` 関数の例の実装です：

```js
const either =
  (f, g) =>
  (...args) =>
    f(...args) || g(...args);
```

そして、2つの関数 `isEven` と `isPositive` を使った `either` 関数の使用例です：

```js
const isEven = (num) => num % 2 === 0;
const isPositive = (num) => num > 0;
const isPositiveOrEven = either(isPositive, isEven);
isPositiveOrEven(4); // true
isPositiveOrEven(3); // true
```

この例では、`isPositiveOrEven` は `4` と `3` の両方に対して `true` を返します。なぜなら、`isEven` は `4` に対して `true` を返し、`isPositive` は `3` に対して `true` を返すからです。
