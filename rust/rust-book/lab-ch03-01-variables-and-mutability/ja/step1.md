# 変数と不変性

「変数を使った値の格納」で述べたように、デフォルトでは変数は不変です。これは、Rustが提供する安全性と並行性を活かしたコードを書くように促す多くの方法の1つです。ただし、変数を可変にするオプションもあります。Rustが不変性を推奨する方法と理由、そして時々それを避けたい理由を探ってみましょう。

変数が不変の場合、値が名前にバインドされると、その値を変更することはできません。これを示すために、`cargo new variables`を使って`project`ディレクトリに新しいプロジェクト`variables`を生成します。

次に、新しい`variables`ディレクトリの中で`src/main.rs`を開き、そのコードを次のコードに置き換えます。まだコンパイルはできません。

ファイル名: `src/main.rs`

```rust
fn main() {
    let x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
}
```

`cargo run`を使ってプログラムを保存して実行します。次の出力のように、不変性エラーに関するエラーメッセージが表示されるはずです。

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
error[E0384]: cannot assign twice to immutable variable `x`
 --> src/main.rs:4:5
  |
2 |     let x = 5;
  |         -
  |         |
  |         first assignment to `x`
  |         help: consider making this binding mutable: `mut x`
3 |     println!("The value of x is: {x}");
4 |     x = 6;
  |     ^^^^^ cannot assign twice to immutable variable
```

この例は、コンパイラがプログラムのエラーを見つけるのにどのように役立つかを示しています。コンパイラのエラーは悔やましいかもしれませんが、実際にはあなたのプログラムが安全に望むことを行っていないことを意味するだけで、あなたが良いプログラマでないことを意味するものではありません！経験豊富なRustプログラマもまだコンパイラのエラーを起こします。

`x`という不変変数に2回目の値を代入しようとしたため、`不変変数`x\`に2回代入できません`というエラーメッセージを受け取りました。

不変と指定された値を変更しようとするときにコンパイル時のエラーが発生することは重要です。なぜなら、このような状況はバグにつながる可能性があるからです。コードの一部が値が決して変わらないという前提で動作し、コードの別の部分がその値を変更する場合、コードの最初の部分が意図通りに動作しなくなる可能性があります。この種のバグの原因は、事後に特定するのが難しい場合があります。特に、2番目のコードが値を変更するのは`たまにのみ`の場合です。Rustコンパイラは、値が変更されないと宣言した場合、本当に変更されないことを保証するので、自分で追跡する必要はありません。したがって、コードを理解しやすくなります。

しかし、可変性は非常に便利で、コードを書きやすくすることができます。変数はデフォルトで不変ですが、第2章でやったように、変数名の前に`mut`を追加することで可変にすることができます。`mut`を追加することで、コードの他の部分がこの変数の値を変更することを示すことで、コードの将来の読者に意図を伝えることもできます。

たとえば、`src/main.rs`を次のように変更しましょう。

ファイル名: `src/main.rs`

```rust
fn main() {
    let mut x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
}
```

このプログラムを実行すると、次のようになります。

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/variables`
The value of x is: 5
The value of x is: 6
```

`mut`を使用すると、`x`にバインドされた値を`5`から`6`に変更することができます。最終的に、可変性を使用するかどうかはあなた次第であり、その特定の状況で何が最も明確かに依存します。
