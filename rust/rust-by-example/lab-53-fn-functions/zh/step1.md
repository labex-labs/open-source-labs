# 函数

函数使用 `fn` 关键字声明。其参数和变量一样要进行类型标注，如果函数返回一个值，则必须在箭头 `->` 之后指定返回类型。

函数中的最后一个表达式将用作返回值。或者，也可以使用 `return` 语句在函数内部提前返回一个值，甚至可以从循环或 `if` 语句内部返回。

让我们用函数重写 FizzBuzz！

```rust
// 与 C/C++ 不同，函数定义的顺序没有限制
fn main() {
    // 我们可以在这里使用这个函数，并在后面的某个地方定义它
    fizzbuzz_to(100);
}

// 返回布尔值的函数
fn is_divisible_by(lhs: u32, rhs: u32) -> bool {
    // 边界情况，提前返回
    if rhs == 0 {
        return false;
    }

    // 这是一个表达式，这里不需要 `return` 关键字
    lhs % rhs == 0
}

// “不”返回值的函数，实际上返回单元类型 `()`
fn fizzbuzz(n: u32) -> () {
    if is_divisible_by(n, 15) {
        println!("fizzbuzz");
    } else if is_divisible_by(n, 3) {
        println!("fizz");
    } else if is_divisible_by(n, 5) {
        println!("buzz");
    } else {
        println!("{}", n);
    }
}

// 当一个函数返回 `()` 时，返回类型可以在签名中省略
fn fizzbuzz_to(n: u32) {
    for n in 1..=n {
        fizzbuzz(n);
    }
}
```
