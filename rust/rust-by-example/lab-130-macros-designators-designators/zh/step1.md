# 指示符

宏的参数以美元符号 `$` 为前缀，并使用一个 _指示符_ 进行类型注释：

```rust
macro_rules! create_function {
    // 此宏接受一个 `ident` 指示符类型的参数，并
    // 创建一个名为 `$func_name` 的函数。
    // `ident` 指示符用于变量/函数名。
    ($func_name:ident) => {
        fn $func_name() {
            // `stringify!` 宏将一个 `ident` 转换为字符串。
            println!("你调用了 {:?}()",
                     stringify!($func_name));
        }
    };
}

// 使用上述宏创建名为 `foo` 和 `bar` 的函数。
create_function!(foo);
create_function!(bar);

macro_rules! print_result {
    // 此宏接受一个 `expr` 类型的表达式，并打印
    // 它及其结果的字符串形式。
    // `expr` 指示符用于表达式。
    ($expression:expr) => {
        // `stringify!` 将按原样把表达式转换为字符串。
        println!("{:?} = {:?}",
                 stringify!($expression),
                 $expression);
    };
}

fn main() {
    foo();
    bar();

    print_result!(1u32 + 1);

    // 记住，代码块也是表达式！
    print_result!({
        let x = 1u32;

        x * x + 2 * x - 1
    });
}
```

以下是一些可用的指示符：

- `block`
- `expr` 用于表达式
- `ident` 用于变量/函数名
- `item`
- `literal` 用于字面常量
- `pat`（_模式_）
- `path`
- `stmt`（_语句_）
- `tt`（_标记树_）
- `ty`（_类型_）
- `vis`（_可见性限定符_）

有关完整列表，请参阅 \[Rust 参考手册\]。
