# エラーメッセージの改善

リスト12-8では、`new`関数にチェックを追加して、インデックス1とインデックス2にアクセスする前にスライスが十分に長いことを確認します。スライスが十分に長くなければ、プログラムはパニックになり、より良いエラーメッセージが表示されます。

ファイル名: `src/main.rs`

```rust
--snip--
fn new(args: &[String]) -> Config {
    if args.len() < 3 {
        panic!("not enough arguments");
    }
    --snip--
```

リスト12-8: 引数の数のチェックを追加する

このコードは、リスト9-13で書いた`Guess::new`関数に似ています。そこでは、`value`引数が有効な値の範囲外の場合に`panic!`を呼び出していました。ここでは値の範囲をチェックする代わりに、`args`の長さが少なくとも`3`であることをチェックし、この条件が満たされているという前提のもとで関数の残りの部分を動作させます。`args`に3つ未満の要素が含まれている場合、この条件は`true`になり、`panic!`マクロを呼び出してプログラムを即座に終了します。

`new`にこれらの数行のコードを追加したので、もう一度引数なしでプログラムを実行して、今のエラーの様子を見てみましょう。

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep`
thread 'main' panicked at 'not enough arguments',
src/main.rs:26:13
note: run with `RUST_BACKTRACE=1` environment variable to display
a backtrace
```

この出力は良くなりました。今では合理的なエラーメッセージがあります。ただし、ユーザーに与える必要のない余分な情報もあります。おそらく、リスト9-13で使用した手法はここでは最適なものではないかもしれません。第9章で説明したように、`panic!`の呼び出しは、使用問題よりもプログラミング上の問題に対してより適切です。代わりに、第9章で学んだもう一つの手法を使用します。つまり、成功またはエラーを示す`Result`を返すことです。
