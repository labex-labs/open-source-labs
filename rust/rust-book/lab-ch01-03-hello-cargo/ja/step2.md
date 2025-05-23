# Cargo を使ってプロジェクトを作成する

Cargo を使って新しいプロジェクトを作成し、最初の「Hello, world!」プロジェクトとどのように異なるか見てみましょう。`project`ディレクトリ（またはコードを保存する場所）に移動します。そして、どのオペレーティングシステムでも、次のコマンドを実行します。

```bash
cd ~/project
cargo new hello_cargo
cd hello_cargo
```

最初のコマンドは、新しいディレクトリと「hello_cargo」という名前のプロジェクトを作成します。私たちはプロジェクト名を「hello_cargo」とし、Cargo は同じ名前のディレクトリにファイルを作成します。

`hello_cargo`ディレクトリに移動して、ファイルを一覧表示します。Cargo が私たちのために 2 つのファイルと 1 つのディレクトリを生成していることがわかります。`Cargo.toml`ファイルと、中に`main.rs`ファイルがある`src`ディレクトリです。

また、新しい Git リポジトリと`.gitignore`ファイルも初期化されています。既存の Git リポジトリ内で`cargo new`を実行すると、Git ファイルは生成されません。`cargo new --vcs=git`を使うことで、この動作をオーバーライドできます。

> 注：Git は一般的なバージョン管理システムです。`--vcs`フラグを使うことで、`cargo new`を使って異なるバージョン管理システムまたはバージョン管理システムを使わないように変更できます。利用可能なオプションを見るには、`cargo new --help`を実行してください。

好きなテキストエディタで`Cargo.toml`を開きます。リスト 1-2 のコードに似ているはずです。

ファイル名：`Cargo.toml`

```toml
[package]
name = "hello_cargo"
version = "0.1.0"
edition = "2021"

[dependencies]
```

リスト 1-2：`cargo new`によって生成された`Cargo.toml`の内容

このファイルは*TOML*（_Tom's Obvious, Minimal Language_）形式で、Cargo の設定形式です。

最初の行の`[package]`は、セクションの見出しで、次の文がパッケージを設定していることを示しています。このファイルにさらに情報を追加するにつれて、他のセクションを追加します。

次の 3 行は、Cargo がプログラムをコンパイルするために必要な設定情報を設定しています。名前、バージョン、および使用する Rust のエディションです。付録 E で`edition`キーについて説明します。

最後の行の`[dependencies]`は、プロジェクトの依存関係をリストするセクションの始まりです。Rust では、コードのパッケージを「クレート」と呼びます。このプロジェクトでは他のクレートは必要ありませんが、第 2 章の最初のプロジェクトでは必要になりますので、そのときにこの依存関係セクションを使います。

次に、`src/main.rs`を開いて見てみましょう。

ファイル名：`src/main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

Cargo があなたのために「Hello, world!」プログラムを生成してくれました。リスト 1-1 で書いたものと同じです！これまでのところ、私たちのプロジェクトと Cargo が生成したプロジェクトの違いは、Cargo がコードを`src`ディレクトリに配置し、トップディレクトリに`Cargo.toml`設定ファイルがあることです。

Cargo はソースファイルを`src`ディレクトリの中に置くことを期待しています。トップレベルのプロジェクトディレクトリは、README ファイル、ライセンス情報、設定ファイル、その他コードに関係のないもの用の場所です。Cargo を使うことで、プロジェクトを整理するのが助けられます。物にはそれぞれ場所があり、すべてがその場所にあります。

「Hello, world!」プロジェクトのように、Cargo を使わないで始めたプロジェクトも、Cargo を使うプロジェクトに変換できます。プロジェクトコードを`src`ディレクトリに移動し、適切な`Cargo.toml`ファイルを作成します。
