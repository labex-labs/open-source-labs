# 引数解析

マッチングを使って簡単な引数を解析することができます。

```rust
use std::env;

fn increase(number: i32) {
    println!("{}", number + 1);
}

fn decrease(number: i32) {
    println!("{}", number - 1);
}

fn help() {
    println!("usage:
match_args <string>
    与えられた文字列を答えとしているかどうかを確認します。
match_args {{increase|decrease}} <integer>
    与えられた整数を 1 増やすか減らします。");
}

fn main() {
    let args: Vec<String> = env::args().collect();

    match args.len() {
        // 引数が渡されていない
        1 => {
            println!("私の名前は'match_args' です。いくつかの引数を渡してみてください！");
        },
        // 1 つの引数が渡された
        2 => {
            match args[1].parse() {
                Ok(42) => println!("これが答えです！"),
                _ => println!("これは答えではありません。"),
            }
        },
        // 1 つのコマンドと 1 つの引数が渡された
        3 => {
            let cmd = &args[1];
            let num = &args[2];
            // 数値を解析する
            let number: i32 = match num.parse() {
                Ok(n) => {
                    n
                },
                Err(_) => {
                    eprintln!("エラー: 2 番目の引数は整数ではありません");
                    help();
                    return;
                },
            };
            // コマンドを解析する
            match &cmd[..] {
                "increase" => increase(number),
                "decrease" => decrease(number),
                _ => {
                    eprintln!("エラー: 無効なコマンド");
                    help();
                },
            }
        },
        // その他のすべてのケース
        _ => {
            // ヘルプメッセージを表示する
            help();
        }
    }
}
```

```shell
$./match_args Rust
これは答えではありません。
$./match_args 42
これが答えです！
$./match_args do something
エラー: 2 番目の引数は整数ではありません
usage:
match_args <string>
    与えられた文字列を答えとしているかどうかを確認します。
match_args {{increase|decrease}} <integer>
    与えられた整数を 1 増やすか減らします。
$./match_args do 42
エラー: 無効なコマンド
usage:
match_args <string>
    与えられた文字列を答えとしているかどうかを確認します。
match_args {{increase|decrease}} <integer>
    与えられた整数を 1 増やすか減らします。
$./match_args increase 42
43
```
