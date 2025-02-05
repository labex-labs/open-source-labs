# 参数解析

匹配可用于解析简单参数：

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
    检查给定字符串是否是答案。
match_args {{increase|decrease}} <整数>
    将给定整数增加或减少一。");
}

fn main() {
    let args: Vec<String> = env::args().collect();

    match args.len() {
        // 未传递参数
        1 => {
            println!("我叫'match_args'。试试传递一些参数！");
        },
        // 传递了一个参数
        2 => {
            match args[1].parse() {
                Ok(42) => println!("这就是答案！"),
                _ => println!("这不是答案。"),
            }
        },
        // 传递了一个命令和一个参数
        3 => {
            let cmd = &args[1];
            let num = &args[2];
            // 解析数字
            let number: i32 = match num.parse() {
                Ok(n) => {
                    n
                },
                Err(_) => {
                    eprintln!("错误：第二个参数不是整数");
                    help();
                    return;
                },
            };
            // 解析命令
            match &cmd[..] {
                "increase" => increase(number),
                "decrease" => decrease(number),
                _ => {
                    eprintln!("错误：无效命令");
                    help();
                },
            }
        },
        // 所有其他情况
        _ => {
            // 显示帮助信息
            help();
        }
    }
}
```

```shell
$./match_args Rust
这不是答案。
$./match_args 42
这就是答案！
$./match_args do something
错误：第二个参数不是整数
usage:
match_args <string>
    检查给定字符串是否是答案。
match_args {increase|decrease} <整数>
    将给定整数增加或减少一。
$./match_args do 42
错误：无效命令
usage:
match_args <string>
    检查给定字符串是否是答案。
match_args {increase|decrease} <整数>
    将给定整数增加或减少一。
$./match_args increase 42
43
```
