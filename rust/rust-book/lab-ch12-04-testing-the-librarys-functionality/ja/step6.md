# 一致する行を格納する

この関数を完成させるには、返す一致する行を格納する方法が必要です。そのために、`for`ループの前に可変ベクトルを作成し、`push`メソッドを呼び出してベクトルに`line`を格納します。`for`ループの後で、ベクトルを返します。これはリスト12-19に示すようになります。

ファイル名: `src/lib.rs`

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

リスト12-19: 一致する行を格納して返すためにする

これで`search`関数は`query`を含む行のみを返すようになり、テストも通過するはずです。テストを実行しましょう。

```bash
$ cargo test
--snip--
running 1 test
test tests::one_result... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0
filtered out
finished in 0.00s
```

テストが通過しましたので、機能することがわかります！

この時点で、テストを通過させたままで同じ機能を維持しながら、検索関数の実装をリファクタリングする機会を検討することができます。検索関数のコードはあまり悪くはありませんが、イテレータのいくつかの便利な機能を利用していません。13章でこの例に戻り、イテレータを詳細に検討し、それをどのように改善するかを見ていきます。
