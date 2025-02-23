# 条件分岐

> ターミナル/SSH を開き、コーディングの練習を始めるには `node` と入力します。

条件分岐は、式が真を返すかどうかをテストするために使用されるコード構造です。条件分岐の非常に一般的な形式は `if...else` 文です。たとえば：

```js
let iceCream = "chocolate";
if (iceCream === "chocolate") {
  console.log("Yay, I love chocolate ice cream!");
} else {
  console.log("Awwww, but chocolate is my favorite…");
}
```

`if ()` の中の式がテストです。これは、厳密な等価演算子（上記の通り）を使用して、変数 `iceCream` と文字列 `chocolate` を比較して、両者が等しいかどうかを確認します。この比較が `true` を返す場合、最初のコードブロックが実行されます。比較が真でない場合、`else` 文の後の 2 番目のコードブロックが代わりに実行されます。
