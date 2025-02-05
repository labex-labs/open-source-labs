# 管道

`std::Child` 结构体表示一个正在运行的子进程，并通过管道公开 `stdin`、`stdout` 和 `stderr` 句柄，以便与底层进程进行交互。

```rust
use std::io::prelude::*;
use std::process::{Command, Stdio};

static PANGRAM: &'static str =
"the quick brown fox jumped over the lazy dog\n";

fn main() {
    // 启动 `wc` 命令
    let process = match Command::new("wc")
                              .stdin(Stdio::piped())
                              .stdout(Stdio::piped())
                              .spawn() {
        Err(why) => panic!("无法启动 wc: {}", why),
        Ok(process) => process,
    };

    // 向 `wc` 的 `stdin` 写入一个字符串。
    //
    // `stdin` 的类型为 `Option<ChildStdin>`，但由于我们知道这个实例一定有一个，所以可以直接 `unwrap` 它。
    match process.stdin.unwrap().write_all(PANGRAM.as_bytes()) {
        Err(why) => panic!("无法写入 wc 的 stdin: {}", why),
        Ok(_) => println!("已将全字母句发送到 wc"),
    }

    // 因为 `stdin` 在上述调用之后不再存在，所以它会被 `drop`，管道也会被关闭。
    //
    // 这非常重要，否则 `wc` 不会开始处理我们刚刚发送的输入。

    // `stdout` 字段的类型也是 `Option<ChildStdout>`，所以也必须解包。
    let mut s = String::new();
    match process.stdout.unwrap().read_to_string(&mut s) {
        Err(why) => panic!("无法读取 wc 的 stdout: {}", why),
        Ok(_) => print!("wc 的响应为:\n{}", s),
    }
}
```
