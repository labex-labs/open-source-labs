# 単体テスト

テストは、非テストコードが期待通りに機能していることを検証する Rust 関数です。テスト関数の本体は通常、いくつかのセットアップを行い、テストしたいコードを実行し、その結果が期待通りであるかどうかをアサートします。

ほとんどの単体テストは、`#[cfg(test)]` 属性付きの `tests` モジュールに記述されます。テスト関数は `#[test]` 属性でマークされます。

テスト関数内の何かがパニックする場合、テストは失敗します。いくつかのヘルパーマクロがあります。

- `assert!(expression)` - 式が `false` と評価される場合にパニックします。
- `assert_eq!(left, right)` と `assert_ne!(left, right)` - それぞれ、左辺と右辺の式が等しいかどうか、および等しくないかどうかをテストします。

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

// これは本当に悪い加算関数で、この例では失敗することを目的としています。
#[allow(dead_code)]
fn bad_add(a: i32, b: i32) -> i32 {
    a - b
}

#[cfg(test)]
mod tests {
    // この便利な慣用句に注意してください: 外側の (モジュールテスト用) スコープから名前をインポートします。
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(1, 2), 3);
    }

    #[test]
    fn test_bad_add() {
        // このアサーションがトリガーされ、テストは失敗します。
        // 注意してください、非公開関数もテストできます！
        assert_eq!(bad_add(1, 2), 3);
    }
}
```

`cargo test` でテストを実行できます。

```shell
$ cargo test

running 2 tests
test tests::test_bad_add... FAILED
test tests::test_add... ok

failures:

---- tests::test_bad_add stdout ----
thread 'tests::test_bad_add' panicked at 'assertion failed: `(left == right)`
  left: `-1`,
 right: `3`', src/lib.rs:21:8
note: Run with $(RUST_BACKTRACE=1) for a backtrace.

failures:
tests::test_bad_add

test result: FAILED. 1 passed
1 failed
0 ignored
0 measured
0 filtered out
```

## テストと `?`

以前の単体テストの例では、戻り値の型はありませんでした。しかし、Rust 2018 では、単体テストが `Result<()>` を返すことができ、それにより `?` を使用できるようになりました！これにより、テストをはるかに簡潔にすることができます。

```rust
fn sqrt(number: f64) -> Result<f64, String> {
    if number >= 0.0 {
        Ok(number.powf(0.5))
    } else {
        Err("negative floats don't have square roots".to_owned())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sqrt() -> Result<(), String> {
        let x = 4.0;
        assert_eq!(sqrt(x)?.powf(2.0), x);
        Ok(())
    }
}
```

詳細については、「エディションガイド」を参照してください。

## パニックのテスト

特定の状況下でパニックするはずの関数をチェックするには、属性 `#[should_panic]` を使用します。この属性は、パニックメッセージのテキストを持つオプションのパラメータ `expected =` を受け付けます。関数が複数の方法でパニックする場合、テストが正しいパニックをテストしていることを確認するのに役立ちます。

```rust
pub fn divide_non_zero_result(a: u32, b: u32) -> u32 {
    if b == 0 {
        panic!("Divide-by-zero error");
    } else if a < b {
        panic!("Divide result is zero");
    }
    a / b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_divide() {
        assert_eq!(divide_non_zero_result(10, 2), 5);
    }

    #[test]
    #[should_panic]
    fn test_any_panic() {
        divide_non_zero_result(1, 0);
    }

    #[test]
    #[should_panic(expected = "Divide result is zero")]
    fn test_specific_panic() {
        divide_non_zero_result(1, 10);
    }
}
```

これらのテストを実行すると、次のようになります。

```shell
$ cargo test

running 3 tests
test tests::test_any_panic... ok
test tests::test_divide... ok
test tests::test_specific_panic... ok

test result: ok. 3 passed
0 failed
0 ignored
0 measured
0 filtered out

Doc-tests tmp-test-should-panic

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

## 特定のテストの実行

特定のテストを実行するには、`cargo test` コマンドにテスト名を指定することができます。

```shell
$ cargo test test_any_panic
running 1 test
test tests::test_any_panic... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
2 filtered out

Doc-tests tmp-test-should-panic

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

複数のテストを実行するには、実行するすべてのテストに一致するテスト名の一部を指定することができます。

```shell
$ cargo test panic
running 2 tests
test tests::test_any_panic... ok
test tests::test_specific_panic... ok

test result: ok. 2 passed
0 failed
0 ignored
0 measured
1 filtered out

Doc-tests tmp-test-should-panic

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

## テストの無視

テストを一部除外するには、`#[ignore]` 属性でテストをマークすることができます。または、コマンド `cargo test -- --ignored` で実行することもできます。

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 2), 4);
    }

    #[test]
    fn test_add_hundred() {
        assert_eq!(add(100, 2), 102);
        assert_eq!(add(2, 100), 102);
    }

    #[test]
    #[ignore]
    fn ignored_test() {
        assert_eq!(add(0, 0), 0);
    }
}
```

```shell
$ cargo test
running 3 tests
test tests::ignored_test... ignored
test tests::test_add... ok
test tests::test_add_hundred... ok

test result: ok. 2 passed
0 failed
1 ignored
0 measured
0 filtered out

Doc-tests tmp-ignore

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out

$ cargo test -- --ignored
running 1 test
test tests::ignored_test... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0 filtered out

Doc-tests tmp-ignore

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```
