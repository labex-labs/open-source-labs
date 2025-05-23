# Rust プログラムの書き込みと実行

次に、新しいソースファイルを作成して`main.rs`と名付けます。Rust ファイルは常に`.rs`拡張子で終わります。ファイル名に複数の単語を使う場合、慣例としてアンダースコアで区切ります。たとえば、`helloworld.rs`ではなく`hello_world.rs`を使います。

さて、先ほど作成した`main.rs`ファイルを開き、リスト 1-1 のコードを入力します。

ファイル名：`main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

リスト 1-1: 「Hello, world!」を表示するプログラム

ファイルを保存して、`~/project/hello_world`ディレクトリのターミナルウィンドウに戻ります。Linux または macOS の場合、以下のコマンドを入力してファイルをコンパイルして実行します。

```bash
$ rustc main.rs
$./main
Hello, world!
```

オペレーティングシステムに関係なく、文字列「Hello, world!」がターミナルに表示されるはずです。この出力が見えない場合は、「トラブルシューティング」を参照して助けを求める方法を探してください。

もし「Hello, world!」が表示されたら、おめでとうございます！公式に Rust プログラムを書きました。あなたは Rust プログラマになりました。ようこそ！
