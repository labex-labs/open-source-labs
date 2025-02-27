# パイプ

`std::Child` 構造体は、実行中の子プロセスを表し、パイプを介して基礎となるプロセスとの相互作用のために `stdin`、`stdout`、および `stderr` ハンドルを公開します。

```rust
use std::io::prelude::*;
use std::process::{Command, Stdio};

static PANGRAM: &'static str =
"the quick brown fox jumped over the lazy dog\n";

fn main() {
    // `wc` コマンドを起動する
    let process = match Command::new("wc")
                               .stdin(Stdio::piped())
                               .stdout(Stdio::piped())
                               .spawn() {
        Err(why) => panic!("couldn't spawn wc: {}", why),
        Ok(process) => process,
    };

    // `wc` の `stdin` に文字列を書き込む。
    //
    // `stdin` は `Option<ChildStdin>` 型ですが、このインスタンスには必ず1つ存在することがわかっているので、直接 `unwrap` できます。
    match process.stdin.unwrap().write_all(PANGRAM.as_bytes()) {
        Err(why) => panic!("couldn't write to wc stdin: {}", why),
        Ok(_) => println!("sent pangram to wc"),
    }

    // 上記の呼び出しの後で `stdin` が存在しなくなるため、`drop` され、パイプが閉じられます。
    //
    // これは非常に重要です。そうでなければ、`wc` は私たちが送信した入力を処理し始めないでしょう。

    // `stdout` フィールドも `Option<ChildStdout>` 型なので、unwrap する必要があります。
    let mut s = String::new();
    match process.stdout.unwrap().read_to_string(&mut s) {
        Err(why) => panic!("couldn't read wc stdout: {}", why),
        Ok(_) => print!("wc responded with:\n{}", s),
    }
}
```
