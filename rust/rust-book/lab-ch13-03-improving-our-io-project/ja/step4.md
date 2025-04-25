# インデックス付けの代わりに反復子トレイトメソッドを使用する

次に、`Config::build`の本体を修正します。`args`は`Iterator`トレイトを実装しているので、それに対して`next`メソッドを呼び出せることがわかります！リスト 13-20 は、リスト 12-23 のコードを更新して、`next`メソッドを使用するようにしています。

ファイル名：`src/lib.rs`

```rust
impl Config {
    pub fn build(
        mut args: impl Iterator<Item = String>,
    ) -> Result<Config, &'static str> {
        args.next();

        let query = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a query string"),
        };

        let file_path = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a file path"),
        };

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

リスト 13-20: 反復子メソッドを使用するように`Config::build`の本体を変更する

`env::args`の返り値の最初の値はプログラムの名前であることを思い出してください。それを無視して次の値に行きたいので、まず`next`を呼び出して返り値は何もせずに済みます。その後、`next`を呼び出して`Config`の`query`フィールドに入れたい値を取得します。`next`が`Some`を返す場合、`match`を使って値を抽出します。`None`を返す場合は、引数が足りないことを意味し、`Err`値を返して早期に終了します。`filename`の値についても同じことを行います。
