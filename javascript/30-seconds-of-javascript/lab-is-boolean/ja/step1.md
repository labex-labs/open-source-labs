# 値が論理値であるかどうかの確認

JavaScript において値が論理値のプリミティブであるかどうかを確認するには、`===` 比較演算子を使った `typeof` 演算子を使用します。

```js
const isBoolean = (val) => typeof val === "boolean";
```

値が論理値であるかどうかを確認するために `isBoolean()` 関数をどのように使用するかの例を以下に示します。

```js
isBoolean(null); // false を返す
isBoolean(false); // true を返す
```

コーディングの練習を始めるには、ターミナル/SSH を開き、`node` と入力します。
