# 程序参数

## 标准库

可以使用 `std::env::args` 来访问命令行参数，它返回一个迭代器，为每个参数生成一个 `String`：

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    // 第一个参数是用于调用程序的路径。
    println!("我的路径是 {}.", args[0]);

    // 其余参数是传递的命令行参数。
    // 像这样调用程序：
    //   $./args arg1 arg2
    println!("我得到了 {:?} 个参数：{:?}。", args.len() - 1, &args[1..]);
}
```

```shell
$./args 1 2 3
我的路径是./args。
我得到了 3 个参数：["1", "2", "3"]。
```

## 第三方库

或者，有许多第三方库在创建命令行应用程序时可以提供额外的功能。[《Rust cookbook》]展示了如何使用更流行的命令行参数第三方库之一 `clap` 的最佳实践。
