# 機能を増やすためのクレートの使用

クレートはRustのソースコードファイルのコレクションであることを覚えておいてください。これまでに構築してきたプロジェクトは「バイナリクレート」であり、実行可能なものです。`rand`クレートは「ライブラリクレート」であり、他のプログラムで使用するためのコードが含まれており、独自で実行することはできません。

Cargoによる外部クレートのコーディネーションこそが、Cargoの本当の強みです。`rand`を使用するコードを書く前に、`Cargo.toml`ファイルを変更して、`rand`クレートを依存関係として追加する必要があります。今すぐそのファイルを開き、Cargoが自動的に作成した`[dependencies]`セクションヘッダの下の末尾に次の行を追加しましょう。このバージョン番号の通りに`rand`を正確に指定してください。そうしないと、このチュートリアルのコード例が機能しなくなる場合があります。

ファイル名：`Cargo.toml`

```tomlrust
[dependencies]
rand = "0.8.5"
```

`Cargo.toml`ファイルでは、ヘッダの後に続くすべてのものは、そのセクションの一部であり、別のセクションが始まるまで続きます。`[dependencies]`では、プロジェクトがどの外部クレートに依存しているか、およびそれらのクレートのどのバージョンが必要かをCargoに伝えます。この場合、セマンティックバージョニング（時々「SemVer」と呼ばれます）を指定して`rand`クレートを指定しています。これは、バージョン番号を記述するための標準です。指定子`0.8.5`は実際には`^0.8.5`の省略形であり、少なくとも0.8.5以上0.9.0未満の任意のバージョンを意味します。

Cargoはこれらのバージョンがバージョン0.8.5と互換性のあるパブリックAPIを持っていると考えており、この仕様により、本章のコードとまだコンパイルできる最新のパッチリリースが得られます。0.9.0以上の任意のバージョンは、以下の例で使用されているAPIと同じものであることは保証されていません。

では、コードを変更せずに、リスト2-2に示すようにプロジェクトをビルドしてみましょう。

```bash
$ cargo build
    Updating crates.io index
  Downloaded rand v0.8.5
  Downloaded libc v0.2.127
  Downloaded getrandom v0.2.7
  Downloaded cfg-if v1.0.0
  Downloaded ppv-lite86 v0.2.16
  Downloaded rand_chacha v0.3.1
  Downloaded rand_core v0.6.3
   Compiling rand_core v0.6.3
   Compiling libc v0.2.127
   Compiling getrandom v0.2.7
   Compiling cfg-if v1.0.0
   Compiling ppv-lite86 v0.2.16
   Compiling rand_chacha v0.3.1
   Compiling rand v0.8.5
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
```

リスト2-2：`rand`クレートを依存関係として追加した後の`cargo build`の実行結果

バージョン番号が異なる場合があります（ただし、SemVerのおかげですべてコードと互換性があります！）、行も異なります（オペレーティングシステムによって異なります）、行の順序も異なる場合があります。

外部依存関係を含めると、Cargoはレジストリからその依存関係が必要とするすべてのものの最新バージョンを取得します。これは、*https://crates.io*のCrates.ioからのデータのコピーです。Crates.ioは、Rustエコシステムの人々が他の人が使用できるようにオープンソースのRustプロジェクトを投稿する場所です。

レジストリを更新した後、Cargoは`[dependencies]`セクションを確認し、既にダウンロードされていないリストにあるクレートをすべてダウンロードします。この場合、依存関係として`rand`のみをリストに記載しましたが、Cargoは`rand`が動作するために依存している他のクレートも取得しました。クレートをダウンロードした後、Rustはそれらをコンパイルし、その後、利用可能な依存関係を使ってプロジェクトをコンパイルします。

何も変更せずにすぐに`cargo build`を再度実行すると、`Finished`行以外には何も出力されません。Cargoは既に依存関係をダウンロードしてコンパイルしていることを知っており、`Cargo.toml`ファイルで依存関係に関する何も変更を加えていません。Cargoはまた、コードに関する何も変更を加えていないことも知っているので、それも再コンパイルしません。何もすることがないので、単に終了します。

`src/main.rs`ファイルを開き、些細な変更を加えて保存してから再ビルドすると、出力は2行だけになります。

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53 secs
```

これらの行は、Cargoが`src/main.rs`ファイルに対する些細な変更でのみビルドを更新することを示しています。依存関係は変更されていないので、Cargoはそれらに対して既にダウンロードしてコンパイルしたものを再利用できることを知っています。
