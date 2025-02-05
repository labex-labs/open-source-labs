# while

当条件为真时，`while` 关键字可用于运行一个循环。

让我们使用 `while` 循环来编写声名狼藉的 FizzBuzz 程序。

```rust
fn main() {
    // 一个计数器变量
    let mut n = 1;

    // 当 `n` 小于 101 时循环
    while n < 101 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }

        // 增加计数器
        n += 1;
    }
}
```
