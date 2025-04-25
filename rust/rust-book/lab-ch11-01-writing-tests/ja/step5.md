# カスタムの失敗メッセージの追加

`assert!`、`assert_eq!`、および `assert_ne!` マクロには、失敗メッセージとともに表示するカスタムメッセージを追加することができます。これは、任意の引数として指定します。必要な引数の後に指定された任意の引数は、`format!` マクロ（「+演算子または format! マクロを使った連結」で説明）に渡されます。これにより、`{}` プレースホルダとそれに入れる値を含む書式文字列が渡せます。カスタムメッセージは、アサーションの意味を文書化するのに役立ちます。テストが失敗したときに、コードの問題が何であるかをよりよく把握することができます。

たとえば、名前で人を迎える関数があり、関数に渡した名前が出力に表示されることをテストしたいとしましょう。

ファイル名：`src/lib.rs`

```rust
pub fn greeting(name: &str) -> String {
    format!("Hello {name}!")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(result.contains("Carol"));
    }
}
```

このプログラムの要件はまだ合意されておらず、挨拶の冒頭の `Hello` のテキストが変更されると思われます。要件が変更されたときにテストを更新する必要がないように、`greeting` 関数から返される値と厳密に等しいことをチェックする代わりに、出力に入力パラメータのテキストが含まれていることをアサートすることにしました。

では、このコードにバグを入れて、`greeting` を変更して `name` を除外して、デフォルトのテスト失敗がどのように見えるか見てみましょう。

```rust
pub fn greeting(name: &str) -> String {
    String::from("Hello!")
}
```

このテストを実行すると、次のような結果になります。

    running 1 test
    test tests::greeting_contains_name... FAILED

    failures:

    ---- tests::greeting_contains_name stdout ----
    thread'main' panicked at 'assertion failed:
    result.contains(\"Carol\")', src/lib.rs:12:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace


    failures:
        tests::greeting_contains_name

この結果は、アサーションが失敗したことと、アサーションがある行を示しています。より役立つ失敗メッセージは、`greeting` 関数からの値を表示するでしょう。`greeting` 関数から得た実際の値で埋められたプレースホルダを持つ書式文字列で構成されるカスタムの失敗メッセージを追加しましょう。

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(
            result.contains("Carol"),
            "Greeting did not contain name, value was `{result}`"
        );
    }

今、テストを実行すると、より情報が豊富なエラーメッセージが表示されます。

    ---- tests::greeting_contains_name stdout ----
    thread'main' panicked at 'Greeting did not contain name, value
    was `Hello!`', src/lib.rs:12:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

テスト出力に実際に得た値が表示されるので、期待したことではなく何が起こったかをデバッグするのに役立ちます。
