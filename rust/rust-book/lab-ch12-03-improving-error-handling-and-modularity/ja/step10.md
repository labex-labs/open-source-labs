# main からのロジックの抽出

コンフィグの解析のリファクタリングが完了したので、次にプログラムのロジックに目を向けましょう。「バイナリプロジェクトの懸念事項の分離」で述べたように、`run`という名前の関数を抽出します。この関数には、現在`main`関数に含まれているコンフィグの設定やエラーの処理に関係のないすべてのロジックを保持させます。完了したら、`main`は簡潔になり、検査によって容易に検証できるようになります。そして、他のすべてのロジックに対してテストを書くことができるようになります。

リスト 12-11 に抽出した`run`関数を示します。今のところ、関数を抽出するという小さな段階的な改善を行っています。まだ`src/main.rs`に関数を定義しています。

ファイル名：`src/main.rs`

```rust
fn main() {
    --snip--

    println!("Searching for {}", config.query);
    println!("In file {}", config.file_path);

    run(config);
}

fn run(config: Config) {
    let contents = fs::read_to_string(config.file_path)
     .expect("Should have been able to read the file");

    println!("With text:\n{contents}");
}

--snip--
```

リスト 12-11: プログラムの残りのロジックを含む`run`関数を抽出する

`run`関数には、今や`main`から残ったすべてのロジックが含まれています。ファイルの読み込みから始まります。`run`関数は`Config`インスタン스를引数として受け取ります。
