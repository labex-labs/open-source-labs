# 否定、非等価

これは、その前にある論理値の逆を返します。`true` を `false` に、などと変えます。等価演算子と一緒に使用される場合、否定演算子は 2 つの値が等しくないかどうかをテストします。

「否定」については、基本的な式は `true` ですが、比較は `false` を返します。なぜなら、それを否定しているからです。

```js
// 否定 (!)
let myVariable = 3;
!(myVariable === 3);
```

「非等価」は、基本的に同じ結果を異なる構文で得ます。ここでは、「`myVariable` が 3 に等しくないか」をテストしています。これは `false` を返します。なぜなら、`myVariable` は 3 に等しいからです。

```js
// 非等価 (!==)
let myVariable = 3;
myVariable !== 3;
```

さらに多くの演算子がありますが、今のところこれだけで十分です。完全な一覧については、[式と演算子](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators) を参照してください。

> **注意：** 計算を行う際にデータ型を混ぜると、奇妙な結果につながることがあります。変数を正しく参照し、期待する結果を得るように注意してください。たとえば、コンソールに `'35' + '25'` を入力してみてください。なぜ期待する結果が得られないのでしょうか？引用符が数字を文字列に変えてしまうため、数字を足すのではなく文字列同士を連結してしまったからです。`35 + 25` を入力すると、2 つの数字の合計が得られます。
