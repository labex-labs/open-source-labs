# 関数

関数はRustコードにおいて非常に一般的です。この言語の中で最も重要な関数の1つである`main`関数を既に見てきました。これは多くのプログラムのエントリポイントです。また、新しい関数を宣言するための`fn`キーワードも見てきました。

`functions`という名前の新しいプロジェクトを作成しましょう。

```bash
cargo new functions
cd functions
```

Rustコードでは、関数名と変数名の慣用的なスタイルとして「スネークケース」を使用しており、すべての文字が小文字で、単語を区切るためにアンダースコアが使われます。以下は、関数定義の例を含むプログラムです。

ファイル名: `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");

    another_function();
}

fn another_function() {
    println!("Another function.");
}
```

Rustでは、`fn`の後に関数名と1組の丸括弧を入力することで関数を定義します。波括弧は、関数本体の始まりと終わりをコンパイラに知らせます。

定義した関数は、関数名の後に1組の丸括弧を入力することで呼び出すことができます。`another_function`はプログラム内に定義されているため、`main`関数の中から呼び出すことができます。ソースコードでは、`main`関数の後に`another_function`を定義しましたが、前に定義しても構いません。Rustは関数をどこで定義するかは気にしません。ただ、呼び出し元が参照できるスコープ内のどこかに定義されていることが重要です。

関数をさらに詳しく調べるために、新しいバイナリプロジェクト`functions`を作成しましょう。`src/main.rs`に`another_function`の例を配置して実行します。以下の出力が表示されるはずです。

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.28s
     Running `target/debug/functions`
Hello, world!
Another function.
```

行は`main`関数内に表示される順序で実行されます。最初に「Hello, world!」のメッセージが表示され、その後`another_function`が呼び出され、そのメッセージが表示されます。
