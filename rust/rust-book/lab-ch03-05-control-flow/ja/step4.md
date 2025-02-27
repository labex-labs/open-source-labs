# let文でのifの使用

`if`は式なので、`let`文の右辺で使用して結果を変数に割り当てることができます。例えば、リスト3-2のようにです。

ファイル名：`src/main.rs`

```rust
fn main() {
    let condition = true;
    let number = if condition { 5 } else { 6 };

    println!("The value of number is: {number}");
}
```

リスト3-2：`if`式の結果を変数に割り当てる

`number`変数は、`if`式の結果に基づいて値に束縛されます。このコードを実行して、何が起こるか見てみましょう：

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/branches`
The value of number is: 5
```

コードブロックはその中の最後の式を評価し、数値自体も式です。この場合、`if`式全体の値はどのコードブロックが実行されるかに依存します。これは、`if`の各アームから結果になり得る値が同じ型でなければならないことを意味します。リスト3-2では、`if`アームと`else`アームの結果はどちらも`i32`整数でした。型が一致しない場合、次の例のように、エラーが発生します：

ファイル名：`src/main.rs`

```rust
fn main() {
    let condition = true;

    let number = if condition { 5 } else { "six" };

    println!("The value of number is: {number}");
}
```

このコードをコンパイルしようとすると、エラーが発生します。`if`と`else`のアームは互換性のない値の型を持っており、Rustはプログラム内の問題の場所を正確に示します：

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
error[E0308]: `if` and `else` have incompatible types
 --> src/main.rs:4:44
  |
4 |     let number = if condition { 5 } else { "six" };
  |                                 -          ^^^^^ expected integer, found
`&str`
  |                                 |
  |                                 expected because of this
```

`if`ブロック内の式は整数を評価し、`else`ブロック内の式は文字列を評価します。これは機能しません。なぜなら、変数は単一の型を持たなければならず、Rustはコンパイル時に`number`変数がどの型であるかを明確に知る必要があるからです。`number`の型を知ることで、コンパイラは`number`を使用するすべての場所で型が有効であることを検証できます。`number`の型が実行時にのみ決定される場合、Rustはそれを行うことができません。コンパイラはより複雑になり、任意の変数に対して複数の仮想型を追跡する必要がある場合、コードに対する保証も少なくなります。
