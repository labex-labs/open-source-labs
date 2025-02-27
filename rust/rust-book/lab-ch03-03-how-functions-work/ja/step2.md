# パラメータ

関数には「パラメータ」を持たせることができます。これは、関数のシグネチャの一部である特別な変数です。関数にパラメータがある場合、それらのパラメータに対して具体的な値を提供することができます。技術的には、具体的な値は「引数」と呼ばれますが、日常会話では、人々は関数の定義内の変数または関数を呼び出す際に渡される具体的な値の両方に対して、「パラメータ」と「引数」の言葉を交換して使用する傾向があります。

このバージョンの`another_function`では、パラメータを追加します。

ファイル名: `src/main.rs`

```rust
fn main() {
    another_function(5);
}

fn another_function(x: i32) {
    println!("The value of x is: {x}");
}
```

このプログラムを実行してみてください。以下の出力が得られるはずです。

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 1.21s
     Running `target/debug/functions`
The value of x is: 5
```

`another_function`の宣言には、`x`という名前の1つのパラメータがあります。`x`の型は`i32`と指定されています。`another_function`に`5`を渡すと、`println!`マクロは、フォーマット文字列の中の`x`を含む波括弧のペアの場所に`5`を置きます。

関数のシグネチャでは、各パラメータの型を宣言する「必要があります」。これは、Rustの設計における意図的な決定です。関数定義に型注釈を必要とすることは、コンパイラがコードの他の場所であなたが何を意味する型を理解するために型注釈を使用する必要がほとんどないことを意味します。関数が期待する型をコンパイラが知っている場合、コンパイラはより有益なエラーメッセージを与えることもできます。

複数のパラメータを定義する場合、パラメータの宣言をコンマで区切ります。次のようになります。

ファイル名: `src/main.rs`

```rust
fn main() {
    print_labeled_measurement(5, 'h');
}

fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {value}{unit_label}");
}
```

この例では、2つのパラメータを持つ`print_labeled_measurement`という名前の関数を作成しています。最初のパラメータは`value`といい、`i32`型です。2番目は`unit_label`といい、型は`char`です。その後、関数は`value`と`unit_label`の両方を含むテキストを表示します。

このコードを実行してみましょう。`functions`プロジェクトの`src/main.rs`ファイルに現在あるプログラムを前の例に置き換え、`cargo run`を使用して実行します。

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/functions`
The measurement is: 5h
```

`value`の値として`5`、`unit_label`の値として`'h'`を関数に渡したので、プログラムの出力にはそれらの値が含まれています。
