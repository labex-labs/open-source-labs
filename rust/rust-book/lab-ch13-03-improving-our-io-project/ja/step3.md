# 直接返される反復子の使用

あなたの I/O プロジェクトの `src/main.rs` ファイルを開きます。このファイルは次のようになっているはずです。

ファイル名: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    --snip--
}
```

まず、リスト12-24にあった`main`関数の始まりを、今度は反復子を使うリスト13-18のコードに変更します。`Config::build`も更新しない限り、これはコンパイルされません。

ファイル名: `src/main.rs`

```rust
fn main() {
    let config =
        Config::build(env::args()).unwrap_or_else(|err| {
            eprintln!("Problem parsing arguments: {err}");
            process::exit(1);
        });

    --snip--
}
```

リスト13-18: `env::args`の返り値を`Config::build`に渡す

`env::args`関数は反復子を返します！反復子の値をベクタに収集してから、スライスを`Config::build`に渡す代わりに、今回は`env::args`から返される反復子の所有権を直接`Config::build`に渡しています。

次に、`Config::build`の定義を更新する必要があります。あなたの I/O プロジェクトの `src/lib.rs` ファイルで、`Config::build`のシグネチャをリスト13-19のように変更しましょう。これもまだコンパイルされません。なぜなら、関数本体も更新する必要があるからです。

ファイル名: `src/lib.rs`

```rust
impl Config {
    pub fn build(
        mut args: impl Iterator<Item = String>,
    ) -> Result<Config, &'static str> {
        --snip--
```

リスト13-19: 反復子を期待するように`Config::build`のシグネチャを更新する

`env::args`関数の標準ライブラリドキュメントによると、それが返す反復子の型は`std::env::Args`で、その型は`Iterator`トレイトを実装し、`String`値を返します。

`Config::build`関数のシグネチャを更新しました。これにより、パラメータ`args`は`&[String]`ではなく、トレイト境界`impl Iterator<Item = String>`を持つジェネリック型になりました。「トレイトをパラメータとして」で議論した`impl Trait`構文のこの使用法は、`args`が`Iterator`型を実装し、`String`項目を返す任意の型であることを意味します。

`args`の所有権を取得し、反復子を使って`args`を変更するため、`args`パラメータの仕様に`mut`キーワードを追加して、可変にすることができます。
