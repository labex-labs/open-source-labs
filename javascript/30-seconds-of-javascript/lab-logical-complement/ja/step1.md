# 論理的補数

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。

関数 `fn` の論理的補数を取得するには、`complement` 関数を使用します。この関数は、任意の引数を渡して `fn` を呼び出した結果に論理否定 (`!`) 演算子を適用する別の関数を返します。

以下はコードの例です：

```js
const complement =
  (fn) =>
  (...args) =>
    !fn(...args);
```

この関数を使用するには、述語関数を定義します。たとえば、与えられた数が偶数の場合に `true` を返す `isEven` です。そして、`complement` 関数を使ってこの関数の論理的補数を取得できます。以下のようになります：

```js
const isEven = (num) => num % 2 === 0;
const isOdd = complement(isEven);
isOdd(2); // false
isOdd(3); // true
```
