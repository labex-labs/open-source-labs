# `should_panic` を使ったパニックのチェック

戻り値をチェックするだけでなく、コードが期待通りにエラー条件を処理することをチェックすることも重要です。たとえば、リスト 9-13 で作成した `Guess` 型を考えてみましょう。`Guess` を使用する他のコードは、`Guess` インスタンスが 1 から 100 の間の値のみを含むことを保証に依存しています。そこで、その範囲外の値で `Guess` インスタンスを作成しようとするとパニックすることを確認するテストを書くことができます。

これは、テスト関数に `should_panic` 属性を追加することで行います。関数内のコードがパニックする場合、テストは合格します。関数内のコードがパニックしない場合、テストは失敗します。

リスト 11-8 は、`Guess::new` のエラー条件が期待通りに発生することを確認するテストを示しています。

    // src/lib.rs
    pub struct Guess {
        value: i32,
    }

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 || value > 100 {
                panic!(
                    "Guess value must be between 1 and 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        #[should_panic]
        fn greater_than_100() {
            Guess::new(200);
        }
    }

リスト 11-8: 条件がパニックを引き起こすことをテストする

`#[should_panic]` 属性を、`#[test]` 属性の後で、それが適用されるテスト関数の前に配置します。このテストが合格したときの結果を見てみましょう。

    running 1 test
    test tests::greater_than_100 - should panic... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

うまくいっているようです！では、コードにバグを入れて、`new` 関数が値が 100 を超えた場合にパニックする条件を削除してみましょう。

    // src/lib.rs
    --snip--

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 {
                panic!(
                    "Guess value must be between 1 and 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

リスト 11-8 のテストを実行すると、失敗します。

    running 1 test
    test tests::greater_than_100 - should panic... FAILED

    failures:

    ---- tests::greater_than_100 stdout ----
    note: test did not panic as expected

    failures:
        tests::greater_than_100

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

この場合、あまり役立たないメッセージが表示されますが、テスト関数を見ると、`#[should_panic]` で注釈付けされていることがわかります。得られた失敗は、テスト関数内のコードがパニックを引き起こさなかったことを意味します。

`should_panic` を使用するテストは不正確である可能性があります。`should_panic` テストは、期待した理由とは別の理由でテストがパニックした場合でも合格します。`should_panic` テストをより正確にするには、`should_panic` 属性にオプションの `expected` パラメータを追加することができます。テストハーネスは、失敗メッセージに提供されたテキストが含まれていることを確認します。たとえば、リスト 11-9 の `Guess` の修正コードを考えてみましょう。ここでは、`new` 関数は値が小さすぎるか大きすぎるかに応じて、異なるメッセージでパニックします。

    // src/lib.rs
    --snip--

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 {
                panic!(
                    "Guess value must be greater than or equal to 1, got {}.",
                    value
                );
            } else if value > 100 {
                panic!(
                    "Guess value must be less than or equal to 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        #[should_panic(expected = "less than or equal to 100")]
        fn greater_than_100() {
            Guess::new(200);
        }
    }

リスト 11-9: 指定された部分文字列を含むパニックメッセージでの `panic!` のテスト

このテストは合格します。なぜなら、`should_panic` 属性の `expected` パラメータに入れた値は、`Guess::new` 関数がパニックするメッセージの部分文字列だからです。この場合、期待する完全なパニックメッセージは `Guess value must be less than or equal to 100, got 200` である可能性があります。どのようなパニックメッセージを指定するかは、パニックメッセージのどれが一意または動的であり、テストをどの程度正確にしたいかに依存します。この場合、パニックメッセージの部分文字列だけでも、テスト関数内のコードが `else if value > 100` のケースを実行することを保証するのに十分です。

`expected` メッセージ付きの `should_panic` テストが失敗したときに何が起こるかを見るために、コードにバグを入れて、`if value < 1` と `else if value > 100` のブロックの本体を入れ替えましょう。

    // src/lib.rs
    --snip--
    if value < 1 {
        panic!(
            "Guess value must be less than or equal to 100, got {}.",
            value
        );
    } else if value > 100 {
        panic!(
            "Guess value must be greater than or equal to 1, got {}.",
            value
        );
    }
    --snip--

今度は、`should_panic` テストを実行すると、失敗します。

    running 1 test
    test tests::greater_than_100 - should panic... FAILED

    failures:

    ---- tests::greater_than_100 stdout ----
    thread'main' panicked at 'Guess value must be greater than or equal to 1, got
    200.', src/lib.rs:13:13
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
    note: panic did not contain expected string
          panic message: `"Guess value must be greater than or equal to 1, got
    200."`,
     expected substring: `"less than or equal to 100"`

    failures:
        tests::greater_than_100

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out;
    finished in 0.00s

失敗メッセージは、このテストが確かに期待通りにパニックしたことを示していますが、パニックメッセージには期待される文字列 `'Guess value must be less than or equal to 100'` が含まれていません。この場合に得られたパニックメッセージは `Guess value must be greater than or equal to 1, got 200` でした。これで、バグがどこにあるかを見つけ始めることができます！
