# 単一のテストを実行する

`cargo test`に任意のテスト関数の名前を渡すことで、そのテストのみを実行できます。

```bash
$ cargo test one_hundred
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.69s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 1 test
test tests::one_hundred... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 2
filtered out; finished in 0.00s
```

名前が`one_hundred`のテストのみが実行されました。他の2つのテストはその名前に一致しませんでした。テストの出力は、最後に`2 filtered out`を表示することで、実行されなかったテストがあることを知らせてくれます。

この方法で複数のテストの名前を指定することはできません。`cargo test`に与えられた最初の値のみが使用されます。ただし、複数のテストを実行する方法があります。
