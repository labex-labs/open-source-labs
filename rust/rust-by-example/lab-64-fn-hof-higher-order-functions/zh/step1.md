# 高阶函数

Rust 提供了高阶函数（HOF）。这些函数接受一个或多个函数，和/或生成一个更有用的函数。高阶函数和惰性迭代器赋予了 Rust 函数式风格。

```rust
fn is_odd(n: u32) -> bool {
    n % 2 == 1
}

fn main() {
    println!("Find the sum of all the squared odd numbers under 1000");
    let upper = 1000;

    // 命令式方法
    // 声明累加器变量
    let mut acc = 0;
    // 迭代：0, 1, 2,... 直到无穷大
    for n in 0.. {
        // 对数字进行平方
        let n_squared = n * n;

        if n_squared >= upper {
            // 如果超过上限则中断循环
            break;
        } else if is_odd(n_squared) {
            // 如果是奇数，则累加值
            acc += n_squared;
        }
    }
    println!("命令式风格：{}", acc);

    // 函数式方法
    let sum_of_squared_odd_numbers: u32 =
        (0..).map(|n| n * n)                             // 所有自然数的平方
            .take_while(|&n_squared| n_squared < upper) // 低于上限
            .filter(|&n_squared| is_odd(n_squared))     // 是奇数的
            .sum();                                     // 求和
    println!("函数式风格：{}", sum_of_squared_odd_numbers);
}
```

`Option` 和 `Iterator` 实现了相当数量的高阶函数。
