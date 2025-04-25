# エラーハンドリングの修正

次に、エラーハンドリングを修正しましょう。`args`ベクトルのインデックス 1 またはインデックス 2 の値にアクセスしようとすると、ベクトルに 3 つ未満の要素が含まれている場合、プログラムがパニックになります。引数なしでプログラムを実行してみてください。出力は次のようになります。

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep`
thread 'main' panicked at 'index out of bounds: the len is 1 but
the index is 1', src/main.rs:27:21
note: run with `RUST_BACKTRACE=1` environment variable to display
a backtrace
```

`index out of bounds: the len is 1 but the index is 1`という行は、プログラマー向けのエラーメッセージです。最終ユーザーにとって、代わりに何をすべきかを理解するのに役立ちません。今すぐそれを修正しましょう。
