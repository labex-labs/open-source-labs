# シャドーイング

第 2 章の予想ゲームのチュートリアルで見たように、以前の変数と同じ名前で新しい変数を宣言することができます。Rust プログラマーは、最初の変数が 2 番目の変数によって「シャドーされる」と言います。これは、変数の名前を使用するときに、コンパイラが見るのは 2 番目の変数であることを意味します。実際のところ、2 番目の変数が最初の変数を上書きし、変数名のすべての使用を自身に引き付けます。それ自体がシャドーされるか、スコープが終了するまでです。次のように、同じ変数名を使用して`let`キーワードを繰り返すことで、変数をシャドーすることができます。

ファイル名：`src/main.rs`

```rust
fn main() {
    let x = 5;

    let x = x + 1;

    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {x}");
    }

    println!("The value of x is: {x}");
}
```

このプログラムはまず`x`を`5`の値にバインドします。次に、`let x =`を繰り返すことで新しい変数`x`を作成し、元の値に`1`を加えます。その結果、`x`の値は`6`になります。次に、波括弧で作成された内側のスコープ内で、3 番目の`let`文も`x`をシャドーし、新しい変数を作成します。前の値に`2`を掛けて`x`の値を`12`にします。そのスコープが終了すると、内側のシャドーイングが終了し、`x`は再び`6`に戻ります。このプログラムを実行すると、次のように出力されます。

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/variables`
The value of x in the inner scope is: 12
The value of x is: 6
```

シャドーイングは、変数を`mut`としてマークすることとは異なります。なぜなら、`let`キーワードを使わずに変数に再代入しようとすると、コンパイル時エラーが発生するからです。`let`を使うことで、値にいくつかの変換を行うことができますが、変換が完了した後は変数を不変にすることができます。

`mut`とシャドーイングのもう 1 つの違いは、`let`キーワードを再度使うときに実際に新しい変数を作成するため、値の型を変更することができる一方で、同じ名前を再利用できることです。たとえば、プログラムがユーザーにいくつの空白文字を入力するかを求め、その入力を数値として格納したい場合を考えてみましょう。

```rust
let spaces = "   ";
let spaces = spaces.len();
```

最初の`spaces`変数は文字列型で、2 番目の`spaces`変数は数値型です。したがって、シャドーイングにより、`spaces_str`や`spaces_num`のような別の名前を考える必要がなくなります。代わりに、よりシンプルな`spaces`という名前を再利用できます。ただし、これを`mut`を使って行おうとすると、次のようにコンパイル時エラーが発生します。

```rust
let mut spaces = "   ";
spaces = spaces.len();
```

エラーメッセージによると、変数の型を変更することはできません。

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
error[E0308]: mismatched types
 --> src/main.rs:3:14
  |
2 |     let mut spaces = "   ";
  |                      ----- expected due to this value
3 |     spaces = spaces.len();
  |              ^^^^^^^^^^^^ expected `&str`, found `usize`
```

ここで、変数の仕組みを理解しましたので、変数が持ちうるさらに多くのデータ型を見てみましょう。
