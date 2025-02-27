# 変数に引数値を保存する

プログラムは現在、コマンドライン引数として指定された値にアクセスできるようになっています。次に、2つの引数の値を変数に保存して、プログラムの残りの部分でそれらの値を使用できるようにする必要があります。それをリスト12-2で行います。

ファイル名: `src/main.rs`

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let query = &args[1];
    let file_path = &args[2];

    println!("Searching for {}", query);
    println!("In file {}", file_path);
}
```

リスト12-2: 検索クエリ引数とファイルパス引数を保持する変数を作成する

ベクターを表示したときに見たように、プログラム名は `args[0]` のベクターの最初の値を占めています。したがって、引数はインデックス1から始まります。`minigrep` が取る最初の引数は、検索する文字列です。したがって、最初の引数への参照を `query` 変数に入れます。2番目の引数はファイルパスになるので、2番目の引数への参照を `file_path` 変数に入れます。

これらの変数の値を一時的に表示して、コードが意図通りに動作していることを確認します。このプログラムを再び `test` と `sample.txt` の引数で実行してみましょう。

```bash
$ cargo run -- test sample.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep test sample.txt`
Searching for test
In file sample.txt
```

素晴らしい！ プログラムが正常に動作しています！ 必要な引数の値が正しい変数に保存されています。後で、ユーザーが引数を提供しないなどの特定の潜在的なエラー状況を処理するためのエラーハンドリングを追加します。今は、その状況を無視して、代わりにファイル読み取り機能を追加する作業に取り組みます。
