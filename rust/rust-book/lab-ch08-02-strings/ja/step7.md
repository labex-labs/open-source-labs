# 文字列をインデックス付けする

多くの他のプログラミング言語では、文字列内の個々の文字にインデックスを付けて参照することは、有効で一般的な操作です。しかし、Rustでインデックス付けの構文を使って`String`の一部にアクセスしようとすると、エラーが発生します。リスト8-19の無効なコードを見てみましょう。

```rust
let s1 = String::from("hello");
let h = s1[0];
```

リスト8-19：`String`にインデックス付けの構文を使用しようとする

このコードは次のエラーを引き起こします。

```bash
error[E0277]: the type `String` cannot be indexed by `{integer}`
 --> src/main.rs:3:13
  |
3 |     let h = s1[0];
  |             ^^^^^ `String` cannot be indexed by `{integer}`
  |
  = help: the trait `Index<{integer}>` is not implemented for
`String`
```

エラーとメモは事情を物語っています。Rustの文字列はインデックス付けをサポートしていません。では、なぜでしょうか？この質問に答えるには、Rustがメモリに文字列を格納する方法について説明する必要があります。
