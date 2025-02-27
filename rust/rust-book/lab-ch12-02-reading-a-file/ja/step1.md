# ファイルの読み込み

次に、`file_path`引数で指定されたファイルを読み込む機能を追加します。まずはテスト用のサンプルファイルが必要です。複数行にわたる少量のテキストといくつかの繰り返し語を含むファイルを使います。リスト12-3にはエミリー・ディキンソンの詩があり、これがうまく機能します！プロジェクトのルートレベルに`_poem.txt_`という名前のファイルを作成し、「I'm Nobody! Who are you?」という詩を入力してください。

ファイル名：poem.txt

    I'm nobody! Who are you?
    Are you nobody, too?
    Then there's a pair of us - don't tell!
    They'd banish us, you know.

    How dreary to be somebody!
    How public, like a frog
    To tell your name the livelong day
    To an admiring bog!

リスト12-3：エミリー・ディキンソンの詩は良いテストケースになります。

テキストを用意したら、`src/main.rs`を編集して、ファイルを読み込むコードを追加します。リスト12-4を参照してください。

ファイル名：`src/main.rs`

```rust
use std::env;
1 use std::fs;

fn main() {
    --snip--
    println!("In file {}", file_path);

  2 let contents = fs::read_to_string(file_path)
       .expect("Should have been able to read the file");

  3 println!("With text:\n{contents}");
}
```

リスト12-4：2番目の引数で指定されたファイルの内容を読み込む

まず、`use`文で標準ライブラリの関連部分をインポートします。ファイルを扱うには`std::fs`が必要です\[1\]。

`main`関数では、新しい文`fs::read_to_string`が`file_path`を受け取り、そのファイルを開き、ファイルの内容の`std::io::Result<String>`を返します\[2\]。

その後、ファイルを読み込んだ後の`contents`の値を表示する一時的な`println!`文を再度追加します。これにより、これまでのプログラムが正常に動作していることを確認できます\[3\]。

最初のコマンドライン引数に任意の文字列を指定し（検索部分はまだ実装していないため）、2番目の引数に`_poem.txt_`ファイルを指定してこのコードを実行してみましょう。

```bash
$ cargo run -- the poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep the poem.txt`
Searching for the
In file poem.txt
With text:
I'm nobody! Who are you?
Are you nobody, too?
Then there's a pair of us - don't tell!
They'd banish us, you know.

How dreary to be somebody!
How public, like a frog
To tell your name the livelong day
To an admiring bog!
```

素晴らしい！コードはファイルを読み込み、その内容を表示しました。しかし、このコードにはいくつかの欠点があります。現在のところ、`main`関数は複数の責務を担っています。一般的には、各関数が1つの機能のみを担当する方が、関数が明確で保守しやすくなります。もう1つの問題は、エラー処理が十分ではないことです。プログラムはまだ小さいので、これらの欠点は大きな問題ではありませんが、プログラムが拡大するにつれて、これらをきれいに修正するのは難しくなります。プログラムを開発する際は、早期にリファクタリングを始めるのが良い練習です。なぜなら、少量のコードをリファクタリングする方がはるかに簡単だからです。次にそれを行います。
