# 複数のテストを実行するためのフィルタリング

テスト名の一部を指定することができ、その値と一致する名前のすべてのテストが実行されます。たとえば、私たちの2つのテストの名前に`add`が含まれているため、`cargo test add`を実行することでそれら2つのテストを実行できます。

```bash
$ cargo test add
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.61s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 2 tests
test tests::add_three_and_two... ok
test tests::add_two_and_two... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 1
filtered out; finished in 0.00s
```

このコマンドは、名前に`add`が含まれるすべてのテストを実行し、`one_hundred`という名前のテストを除外しました。また、テストが含まれるモジュールもテスト名の一部になることに注意してください。したがって、モジュール名でフィルタリングすることで、モジュール内のすべてのテストを実行できます。
