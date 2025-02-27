# cargo install を使ったバイナリのインストール

`cargo install` コマンドを使うと、バイナリクレートをローカルにインストールして使用できます。これはシステムパッケージを置き換えるものではありません。これは、Rust 開発者が *https://crates.io* で他の人が共有したツールをインストールするための便利な方法です。ただし、バイナリターゲットを持つパッケージのみをインストールできます。「バイナリターゲット」とは、クレートに `src/main.rs` ファイルまたはバイナリとして指定された別のファイルがある場合に作成される実行可能なプログラムで、独自では実行できないライブラリターゲットとは対照的で、他のプログラム内に含めるのに適しています。通常、クレートは _README_ ファイルに、クレートがライブラリであるか、バイナリターゲットを持つか、または両方を持つかに関する情報があります。

`cargo install` でインストールされたすべてのバイナリは、インストールルートの `bin` フォルダに保存されます。`rustup.rs` を使って Rust をインストールし、カスタム設定がない場合、このディレクトリは `$HOME/.cargo/bin` になります。`cargo install` でインストールしたプログラムを実行できるようにするには、このディレクトリを `$PATH` に追加してください。

たとえば、12章では、ファイルを検索するための `grep` ツールの Rust 実装である `ripgrep` があることを紹介しました。`ripgrep` をインストールするには、次のコマンドを実行できます。

```bash
$ cargo install ripgrep
    Updating crates.io index
  Downloaded ripgrep v13.0.0
  Downloaded 1 crate (243.3 KB) in 0.88s
  Installing ripgrep v13.0.0
   --snip--
   Compiling ripgrep v13.0.0
    Finished release [optimized + debuginfo] target(s) in 3m 10s
  Installing ~/.cargo/bin/rg
   Installed package `ripgrep v13.0.0` (executable `rg`)
```

出力の2番目の最後の行は、インストールされたバイナリの場所と名前を示しており、`ripgrep` の場合、それは `rg` です。前述のように、インストールディレクトリが `$PATH` にある限り、`rg --help` を実行して、より高速で Rust なファイル検索ツールを使い始めることができます！
