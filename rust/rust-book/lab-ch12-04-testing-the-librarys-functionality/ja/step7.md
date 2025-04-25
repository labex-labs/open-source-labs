# run 関数で search 関数を使用する

`search`関数が機能し、テストに合格したので、`run`関数から`search`を呼び出す必要があります。`config.query`の値と、`run`がファイルから読み取った`contents`を`search`関数に渡す必要があります。そして`run`は、`search`から返された各行を出力します。

ファイル名：`src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    for line in search(&config.query, &contents) {
        println!("{line}");
    }

    Ok(())
}
```

まだ`for`ループを使って、`search`から返された各行を取得して出力しています。

これで、全体のプログラムが機能するはずです！試してみましょう。まずは、エミリー・ディキンソンの詩から正確に 1 行を返す単語「frog」を使ってみます。

```bash
$ cargo run -- frog poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.38s
     Running `target/debug/minigrep frog poem.txt`
How public, like a frog
```

素敵！次に、「body」のように複数の行と一致する単語を試してみましょう。

```bash
$ cargo run -- body poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep body poem.txt`
I'm nobody! Who are you?
Are you nobody, too?
How dreary to be somebody!
```

最後に、詩のどこにもない単語「monomorphization」を検索したときに、何も行が返されないことを確認しましょう。

```bash
$ cargo run -- monomorphization poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep monomorphization poem.txt`
```

素晴らしい！私たちは古典的なツールのミニバージョンを自作し、アプリケーションの構造についてたくさん学びました。また、ファイルの入出力、ライフタイム、テスト、コマンドライン解析についても少し学びました。

このプロジェクトを締めくくるために、環境変数の使い方と標準エラーへの出力方法を簡単に示します。これらはコマンドラインプログラムを書く際に便利です。
