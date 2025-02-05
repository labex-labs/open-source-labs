# 重载

宏可以被重载以接受不同的参数组合。在这方面，`macro_rules!` 的工作方式类似于 `match` 块：

```rust
// `test!` 将根据你调用它的方式以不同方式比较 `$left` 和 `$right`：
macro_rules! test {
    // 参数不需要用逗号分隔。
    // 可以使用任何模板！
    ($left:expr; and $right:expr) => {
        println!("{:?} and {:?} is {:?}",
                 stringify!($left),
                 stringify!($right),
                 $left && $right)
    };
    // ^ 每个分支必须以分号结尾。
    ($left:expr; or $right:expr) => {
        println!("{:?} or {:?} is {:?}",
                 stringify!($left),
                 stringify!($right),
                 $left || $right)
    };
}

fn main() {
    test!(1i32 + 1 == 2i32; and 2i32 * 2 == 4i32);
    test!(true; or false);
}
```
