# 大文字小文字を区別しない検索関数の失敗テストの作成

まず、環境変数に値がある場合に呼び出される新しい`search_case_insensitive`関数を追加します。TDD プロセスに従い続けるので、最初のステップは再び失敗するテストを書くことです。新しい`search_case_insensitive`関数に対する新しいテストを追加し、2 つのテスト間の違いを明確にするために、古いテストを`one_result`から`case_sensitive`にリネームします。リスト 12-20 に示すようになります。

ファイル名：`src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case_sensitive() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Duct tape.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents)
        );
    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Trust me.";

        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        );
    }
}
```

リスト 12-20: 追加する大文字小文字を区別しない関数に対する新しい失敗テストの追加

古いテストの`contents`も編集したことに注意してください。大文字の*D*で`"Duct tape."`という文字列を含む新しい行を追加しました。これは、大文字小文字を区別して検索する場合、クエリ`"duct"`と一致しないはずです。このように古いテストを変更することで、既に実装した大文字小文字を区別した検索機能が偶発的に破壊されないことを確認できます。このテストは現在通るはずで、大文字小文字を区別しない検索の作業中も通り続けるはずです。

大文字小文字を区別しない検索の新しいテストでは、クエリとして`"rUsT"`を使用しています。追加する`search_case_insensitive`関数では、クエリ`"rUsT"`は、大文字の*R*で`"Rust:"`を含む行と一致し、`"Trust me."`の行とも一致するはずです。両方ともクエリとは大文字小文字が異なります。これが失敗するテストで、`search_case_insensitive`関数をまだ定義していないため、コンパイルに失敗します。リスト 12-16 の`search`関数と同じように、常に空のベクトルを返すスケルトン実装を追加して、テストがコンパイルされて失敗するのを確認しても構いません。
