# 引数解析の抽出

コマンドライン引数を解析する機能を、`main`がコマンドライン解析ロジックを`src/lib.rs`に移動する準備として呼び出す関数に抽出します。リスト12-5は、`main`の新しい開始部分を示しており、新しい関数`parse_config`を呼び出しています。この関数は、当面は`src/main.rs`で定義します。

ファイル名: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let (query, file_path) = parse_config(&args);

    --snip--
}

fn parse_config(args: &[String]) -> (&str, &str) {
    let query = &args[1];
    let file_path = &args[2];

    (query, file_path)
}
```

リスト12-5: `main`から`parse_config`関数を抽出する

コマンドライン引数をまだベクトルに収集していますが、`main`関数内でインデックス1の引数値を`query`変数に、インデックス2の引数値を`file_path`変数に代入する代わりに、ベクトル全体を`parse_config`関数に渡します。そして`parse_config`関数が、どの引数がどの変数に入るかを決定するロジックを保持し、値を`main`に戻します。`main`内では依然として`query`と`file_path`変数を作成しますが、コマンドライン引数と変数がどのように対応するかを決定する責任は`main`にはもはやありません。

この再構築は、私たちの小さなプログラムにとってはやりすぎかのように見えるかもしれませんが、小さな段階で徐々にリファクタリングしています。この変更を行った後、再度プログラムを実行して、引数解析がまだ機能することを確認しましょう。問題が発生したときに原因を特定するのに役立つように、頻繁に進捗状況を確認するのは良いことです。
