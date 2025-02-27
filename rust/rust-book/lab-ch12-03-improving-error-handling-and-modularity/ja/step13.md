# コードをライブラリクレートに分割する

これまでのところ、私たちの`minigrep`プロジェクトは順調に進んでいます！ ここでは、`src/main.rs`ファイルを分割し、一部のコードを`src/lib.rs`ファイルに移動します。これにより、コードをテストできるようになり、責任が少ない`src/main.rs`ファイルを持つことができます。

`src/main.rs`にある`main`関数に含まれていないすべてのコードを`src/lib.rs`に移動しましょう。

- `run`関数の定義
- 関連する`use`文
- `Config`の定義
- `Config::build`関数の定義

`src/lib.rs`の内容は、リスト12-13に示すシグネチャになるはずです（簡略化のため、関数の本体は省略しています）。これは、リスト12-14で`src/main.rs`を修正するまではコンパイルされません。

ファイル名: `src/lib.rs`

```rust
use std::error::Error;
use std::fs;

pub struct Config {
    pub query: String,
    pub file_path: String,
}

impl Config {
    pub fn build(
        args: &[String],
    ) -> Result<Config, &'static str> {
        --snip--
    }
}

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    --snip--
}
```

リスト12-13: `Config`と`run`を`src/lib.rs`に移動する

`pub`キーワードを頻繁に使用しています。`Config`、そのフィールドと`build`メソッド、および`run`関数に対してです。これで、テストできるパブリックAPIを持つライブラリクレートができました！

次に、`src/lib.rs`に移動したコードを`src/main.rs`のバイナリクレートのスコープに持ち込む必要があります。これは、リスト12-14に示すようになります。

ファイル名: `src/main.rs`

```rust
use std::env;
use std::process;

use minigrep::Config;

fn main() {
    --snip--
    if let Err(e) = minigrep::run(config) {
        --snip--
    }
}
```

リスト12-14: `src/main.rs`で`minigrep`ライブラリクレートを使用する

`use minigrep::Config`行を追加して、ライブラリクレートから`Config`型をバイナリクレートのスコープに持ち込み、`run`関数にクレート名を接頭辞として付けます。これで、すべての機能が接続され、正常に動作するはずです。`cargo run`でプログラムを実行し、すべてが正しく動作することを確認しましょう。

えーっと！ 大変な作業でしたが、これで将来の成功のための基盤が整いました。今ではエラー処理がはるかに簡単になり、コードもよりモジュール化されています。これ以降、ほとんどの作業は`src/lib.rs`で行われます。

この新しいモジューラリティを生かして、古いコードでは難しかったことを新しいコードでは簡単にできることを行いましょう。テストを書きます！
