# if/else

使用 `if`-`else` 进行分支操作与其他语言类似。与许多语言不同的是，布尔条件不需要用括号括起来，并且每个条件后面都跟着一个代码块。`if`-`else` 条件语句是表达式，并且所有分支必须返回相同的类型。

```rust
fn main() {
    let n = 5;

    if n < 0 {
        print!("{} is negative", n);
    } else if n > 0 {
        print!("{} is positive", n);
    } else {
        print!("{} is zero", n);
    }

    let big_n =
        if n < 10 && n > -10 {
            println!(", and is a small number, increase ten-fold");

            // 此表达式返回一个 `i32` 类型的值。
            10 * n
        } else {
            println!(", and is a big number, halve the number");

            // 此表达式也必须返回一个 `i32` 类型的值。
            n / 2
            // TODO ^ 尝试用分号抑制此表达式。
        };
    //   ^ 别忘了在这里加分号！所有 `let` 绑定都需要它。

    println!("{} -> {}", n, big_n);
}
```
