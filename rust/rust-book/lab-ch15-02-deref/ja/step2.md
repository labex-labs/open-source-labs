# ポインタを辿って値を取得する

通常の参照はポインタの一種であり、ポインタを考える一つの方法は、他の場所に格納されている値への矢印として考えることです。リスト 15-6 では、`i32`型の値に対する参照を作成し、その参照を辿って値を取得するために参照演算子を使用しています。

ファイル名：`src/main.rs`

```rust
fn main() {
  1 let x = 5;
  2 let y = &x;

  3 assert_eq!(5, x);
  4 assert_eq!(5, *y);
}
```

リスト 15-6: 参照演算子を使って`i32`型の値に対する参照を辿る

変数`x`は`i32`型の値`5`を保持しています\[1\]。`y`を`x`への参照に等しく設定します\[2\]。`x`が`5`に等しいことをアサートできます\[3\]。しかし、`y`に格納されている値についてアサートを行う場合、参照演算子`*y`を使用して参照先の値を辿る必要があります（したがって「参照解除」）。そうすることでコンパイラが実際の値を比較できるようになります\[4\]。`y`の参照を解除すると、`y`が指し示す整数値にアクセスでき、それを`5`と比較できるようになります。

代わりに`assert_eq!(5, y);`と書こうとすると、次のコンパイルエラーが発生します。

```bash
error[E0277]: can't compare `{integer}` with `&{integer}`
 --> src/main.rs:6:5
  |
6 |     assert_eq!(5, y);
  |     ^^^^^^^^^^^^^^^^ no implementation for `{integer} ==
&{integer}`
  |
  = help: the trait `PartialEq<&{integer}>` is not implemented
for `{integer}`
```

数値と数値への参照を比較することはできません。なぜなら、それらは異なる型だからです。参照先の値を辿るためには、参照演算子を使用する必要があります。
