# 関数の出力を表示する

既定では、テストが合格した場合、Rustのテストライブラリは標準出力に印刷されたものをすべてキャプチャします。たとえば、テスト内で`println!`を呼び出し、テストが合格した場合、端末には`println!`の出力は表示されません。テストが合格したことを示す行のみが表示されます。テストが失敗した場合、標準出力に印刷されたものとその他の失敗メッセージが表示されます。

例として、リスト11-10には、パラメータの値を印刷して10を返す単純な関数と、合格するテストと失敗するテストがあります。

ファイル名: `src/lib.rs`

```rust
fn prints_and_returns_10(a: i32) -> i32 {
    println!("I got the value {a}");
    10
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn this_test_will_pass() {
        let value = prints_and_returns_10(4);
        assert_eq!(10, value);
    }

    #[test]
    fn this_test_will_fail() {
        let value = prints_and_returns_10(8);
        assert_eq!(5, value);
    }
}
```

リスト11-10: `println!`を呼び出す関数のテスト

`cargo test`でこれらのテストを実行すると、次の出力が表示されます。

    running 2 tests
    test tests::this_test_will_pass... ok
    test tests::this_test_will_fail... FAILED

    failures:

    ---- tests::this_test_will_fail stdout ----
    1 I got the value 8
    thread 'main' panicked at 'assertion failed: `(left == right)`
      left: `5`,
     right: `10`', src/lib.rs:19:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::this_test_will_fail

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

合格するテストを実行する際に印刷される`I got the value 4`は、この出力のどこにも表示されていないことに注意してください。その出力はキャプチャされています。失敗したテストの出力`I got the value 8` \[1\] は、テストの要約出力のセクションに表示され、テストの失敗原因も示されています。

合格するテストの印刷値も見たい場合は、Rustに`--show-output`を使って成功したテストの出力も表示するように指示できます。

```bash
cargo test -- --show-output
```

`--show-output`フラグを使って再度リスト11-10のテストを実行すると、次の出力が表示されます。

    running 2 tests
    test tests::this_test_will_pass... ok
    test tests::this_test_will_fail... FAILED

    successes:

    ---- tests::this_test_will_pass stdout ----
    I got the value 4


    successes:
        tests::this_test_will_pass

    failures:

    ---- tests::this_test_will_fail stdout ----
    I got the value 8
    thread 'main' panicked at 'assertion failed: `(left == right)`
      left: `5`,
     right: `10`', src/lib.rs:19:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::this_test_will_fail

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s
