# 各行をクエリで検索する

次に、現在の行がクエリ文字列を含んでいるかどうかを確認します。幸いなことに、文字列にはこれを行うための便利な`contains`メソッドがあります！`search`関数に`contains`メソッドの呼び出しを追加します。これはリスト 12-18 に示すようになります。ただし、これはまだコンパイルされません。

ファイル名：`src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    for line in contents.lines() {
        if line.contains(query) {
            // do something with line
        }
    }
}
```

リスト 12-18: 行が`query`の文字列含んでいるかどうかを確認する機能を追加する

今のところ、機能を追加しています。コードをコンパイルするには、関数シグネチャで示した通り、本体から値を返す必要があります。
