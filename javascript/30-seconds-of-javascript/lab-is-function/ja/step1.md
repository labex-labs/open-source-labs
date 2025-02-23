# 値が関数であるかどうかの確認

値が関数であるかどうかを確認するには、`typeof` 演算子を `function` プリミティブとともに使用できます。

与えられた値が関数であるかどうかを確認する関数の例を以下に示します。

```js
const isFunction = (val) => typeof val === "function";
```

これを以下のように使用できます。

```js
isFunction("x"); // false
isFunction((x) => x); // true
```

コーディングの練習を始めるには、ターミナル/SSH を開き、`node` と入力します。
