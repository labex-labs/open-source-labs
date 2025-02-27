# Cargoプロジェクトのビルドと実行

次に、Cargoを使って「Hello, world!」プログラムをビルドして実行するときの違いを見てみましょう！`hello_cargo`ディレクトリから、次のコマンドを入力してプロジェクトをビルドします。

```bash
$ cargo build
   Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 2.85 secs
```

このコマンドは、実行可能ファイルを現在のディレクトリではなく`target/debug/hello_cargo`に作成します。デフォルトのビルドはデバッグビルドなので、Cargoはバイナリを`debug`という名前のディレクトリに置きます。このコマンドで実行可能ファイルを実行できます。

```bash
$./target/debug/hello_cargo
Hello, world!
```

すべてがうまくいけば、「Hello, world!」がターミナルに表示されるはずです。最初に`cargo build`を実行すると、Cargoがトップレベルに新しいファイル*Cargo.lock*を作成することもあります。このファイルは、プロジェクトの依存関係の正確なバージョンを追跡します。このプロジェクトには依存関係がないので、ファイルは少し空っぽです。このファイルを手動で変更する必要はありません。Cargoがその内容を管理してくれます。

私たちは先ほど`cargo build`でプロジェクトをビルドし、`./target/debug/hello_cargo`で実行しましたが、`cargo run`を使ってコードをコンパイルしてから、結果の実行可能ファイルを1つのコマンドで実行することもできます。

```bash
$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
     Running `target/debug/hello_cargo`
Hello, world!
```

`cargo run`を使う方が、`cargo build`を実行してからバイナリの完全なパスを使う必要を覚えるよりも便利なので、ほとんどの開発者は`cargo run`を使っています。

今回は、Cargoが`hello_cargo`をコンパイルしていることを示す出力が見られなかったことに注意してください。Cargoはファイルが変更されていないことを判断したので、再ビルドせずにバイナリを実行しました。ソースコードを変更していた場合、Cargoは実行前にプロジェクトを再ビルドし、次の出力が表示されました。

```bash
$ cargo run
   Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.33 secs
     Running `target/debug/hello_cargo`
Hello, world!
```

Cargoには`cargo check`というコマンドもあります。このコマンドは、コードがコンパイルできるかどうかを迅速に確認しますが、実行可能ファイルは生成しません。

```bash
$ cargo check
   Checking hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.32 secs
```

なぜ実行可能ファイルが必要ないのでしょうか？たいていの場合、`cargo check`は`cargo build`よりもはるかに高速です。なぜなら、実行可能ファイルを生成するステップを省略するからです。コードを書いている間に作業を継続的に確認している場合、`cargo check`を使うことで、プロジェクトがまだコンパイルできるかどうかを知らせるプロセスが高速化されます！そのため、多くのRustプログラマは、プログラムを書いている間に定期的に`cargo check`を実行して、コンパイルできることを確認します。そして、実行可能ファイルを使う準備ができたら`cargo build`を実行します。

ここまでで学んだCargoについてのことをまとめましょう。

- `cargo new`を使ってプロジェクトを作成できます。
- `cargo build`を使ってプロジェクトをビルドできます。
- `cargo run`を使って1つのステップでプロジェクトをビルドして実行できます。
- `cargo check`を使って、エラーをチェックするためにバイナリを生成せずにプロジェクトをビルドできます。
- ビルドの結果をコードと同じディレクトリに保存する代わりに、Cargoはそれを`target/debug`ディレクトリに保存します。

Cargoを使うもう1つの利点は、どのオペレーティングシステムを使っているかに関係なく、コマンドが同じであることです。これ以降、LinuxとmacOSとWindowsに関する特定の指示は不再提供します。
