# 使用循环标签来区分多个循环

如果你有嵌套循环，`break` 和 `continue` 此时应用于最内层循环。你可以选择为一个循环指定一个 _循环标签_，然后将其与 `break` 或 `continue` 一起使用，以指定这些关键字应用于带标签的循环，而不是最内层循环。循环标签必须以单引号开头。下面是一个有两个嵌套循环的示例：

```rust
fn main() {
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("End count = {count}");
}
```

外层循环有标签 `'counting_up`，它将从 0 递增到 2。没有标签的内层循环从 10 递减到 9。第一个没有指定标签的 `break` 将仅退出内层循环。`break 'counting_up;` 语句将退出外层循环。这段代码打印：

       正在编译 loops v0.1.0 (file:///projects/loops)
        已完成开发 [未优化 + 调试信息] 目标，耗时 0.58 秒
         正在运行 `target/debug/loops`
    count = 0
    remaining = 10
    remaining = 9
    count = 1
    remaining = 10
    remaining = 9
    count = 2
    remaining = 10
    End count = 2
