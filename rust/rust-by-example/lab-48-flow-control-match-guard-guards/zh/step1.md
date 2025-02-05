# 守卫

可以添加一个 `match` **守卫** 来过滤分支。

```rust
#[allow(dead_code)]
enum Temperature {
    Celsius(i32),
    Fahrenheit(i32),
}

fn main() {
    let temperature = Temperature::Celsius(35);
    // ^ TODO 尝试为 `temperature` 设置不同的值

    match temperature {
        Temperature::Celsius(t) if t > 30 => println!("{}摄氏度高于30摄氏度", t),
        // `if condition` 部分 ^ 是一个守卫
        Temperature::Celsius(t) => println!("{}摄氏度低于30摄氏度", t),

        Temperature::Fahrenheit(t) if t > 86 => println!("{}华氏度高于86华氏度", t),
        Temperature::Fahrenheit(t) => println!("{}华氏度低于86华氏度", t),
    }
}
```

请注意，在检查匹配表达式是否覆盖了所有模式时，编译器不会考虑守卫条件。

```rust
fn main() {
    let number: u8 = 4;

    match number {
        i if i == 0 => println!("零"),
        i if i > 0 => println!("大于零"),
        // _ => unreachable!("Should never happen."),
        // TODO ^ 取消注释以修复编译
    }
}
```
