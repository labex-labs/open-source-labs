# Hello, Cargo

Cargo は Rust のビルドシステム兼パッケージマネージャです。ほとんどの Rust プログラマはこのツールを使って Rust プロジェクトを管理しています。なぜなら、Cargo はコードのビルド、コードが依存するライブラリのダウンロード、そしてそれらのライブラリのビルドなど、たくさんのタスクを代行してくれるからです。（コードが必要とするライブラリを「依存関係」と呼びます。）

これまでに書いたような最もシンプルな Rust プログラムには、依存関係はありません。もし「Hello, world!」プロジェクトを Cargo でビルドした場合、Cargo のうちコードのビルドを担当する部分のみが使われます。より複雑な Rust プログラムを書くようになると、依存関係を追加するようになりますが、Cargo を使ってプロジェクトを始めると、依存関係の追加がはるかに簡単になります。

ほとんどの Rust プロジェクトが Cargo を使っているため、この本の残りの部分では、あなたも Cargo を使っていると仮定しています。もし「インストール」で説明した公式インストーラを使って Rust をインストールした場合、Cargo も一緒にインストールされます。もし他の方法で Rust をインストールした場合は、ターミナルに次のコマンドを入力して Cargo がインストールされているかどうかを確認してください。

```bash
cargo --version
```

バージョン番号が表示されれば、インストールされています！「コマンドが見つかりません」などのエラーが表示された場合は、インストール方法のドキュメントを見て、Cargo を個別にインストールする方法を確認してください。
