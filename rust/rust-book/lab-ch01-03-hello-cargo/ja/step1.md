# Hello, Cargo

CargoはRustのビルドシステム兼パッケージマネージャです。ほとんどのRustプログラマはこのツールを使ってRustプロジェクトを管理しています。なぜなら、Cargoはコードのビルド、コードが依存するライブラリのダウンロード、そしてそれらのライブラリのビルドなど、たくさんのタスクを代行してくれるからです。（コードが必要とするライブラリを「依存関係」と呼びます。）

これまでに書いたような最もシンプルなRustプログラムには、依存関係はありません。もし「Hello, world!」プロジェクトをCargoでビルドした場合、Cargoのうちコードのビルドを担当する部分のみが使われます。より複雑なRustプログラムを書くようになると、依存関係を追加するようになりますが、Cargoを使ってプロジェクトを始めると、依存関係の追加がはるかに簡単になります。

ほとんどのRustプロジェクトがCargoを使っているため、この本の残りの部分では、あなたもCargoを使っていると仮定しています。もし「インストール」で説明した公式インストーラを使ってRustをインストールした場合、Cargoも一緒にインストールされます。もし他の方法でRustをインストールした場合は、ターミナルに次のコマンドを入力してCargoがインストールされているかどうかを確認してください。

```bash
cargo --version
```

バージョン番号が表示されれば、インストールされています！「コマンドが見つかりません」などのエラーが表示された場合は、インストール方法のドキュメントを見て、Cargoを個別にインストールする方法を確認してください。
