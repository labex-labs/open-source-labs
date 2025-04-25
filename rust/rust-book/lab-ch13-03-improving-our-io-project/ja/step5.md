# 反復子アダプタを使ってコードを明確にする

I/O プロジェクトの `search` 関数でも反復子を利用できます。ここでは、リスト 12-19 にあったものと同じように、リスト 13-21 に再現しています。

ファイル名：`src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains(query) {
            results.push(line);
        }
    }

    results
}
```

リスト 13-21: リスト 12-19 の`search`関数の実装

反復子アダプタメソッドを使って、このコードをもっと簡潔に書くことができます。これにより、中間の可変な`results`ベクタを持たなくて済むようになります。関数型プログラミングスタイルでは、コードを明確にするために可変状態の量を最小限に抑えることが好まれます。可変状態を削除することで、将来的に並列で検索を行うような機能強化が可能になるかもしれません。なぜなら、`results`ベクタへの同時アクセスを管理する必要がなくなるからです。リスト 13-22 にこの変更を示します。

ファイル名：`src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    contents
     .lines()
     .filter(|line| line.contains(query))
     .collect()
}
```

リスト 13-22: `search`関数の実装で反復子アダプタメソッドを使用する

`search`関数の目的は、`contents`の中で`query`を含むすべての行を返すことです。リスト 13-16 の`filter`の例と同様に、このコードは`filter`アダプタを使って、`line.contains(query)`が`true`を返す行だけを残します。その後、`collect`を使って一致する行を別のベクタに収集します。はるかに簡単です！`search_case_insensitive`関数でも反復子メソッドを使う同じ変更を自由に行ってください。
