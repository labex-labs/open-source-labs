# 闭包

闭包是能够捕获封闭环境的函数。例如，一个捕获 `x` 变量的闭包：

```rust
|val| val + x
```

闭包的语法和功能使其在即时使用时非常方便。调用闭包与调用函数完全一样。然而，输入和返回类型 _可以_ 被推断出来，并且输入变量名 _必须_ 被指定。

闭包的其他特点包括：

- 在输入变量周围使用 `||` 而不是 `()`。
- 对于单个表达式，可选的主体分隔符 (`{}`)（否则是必需的）。
- 能够捕获外部环境变量。

```rust
fn main() {
    let outer_var = 42;

    // 普通函数不能引用封闭环境中的变量
    //fn function(i: i32) -> i32 { i + outer_var }
    // TODO：取消注释上面一行并查看编译器错误。编译器
    // 建议我们定义一个闭包代替。

    // 闭包是匿名的，这里我们将它们绑定到引用上
    // 注释与函数注释相同，但可以省略
    // 包围主体的 `{}` 也可以省略。这些无名函数
    // 被赋给适当命名的变量。
    let closure_annotated = |i: i32| -> i32 { i + outer_var };
    let closure_inferred  = |i     |          i + outer_var  ;

    // 调用闭包。
    println!("closure_annotated: {}", closure_annotated(1));
    println!("closure_inferred: {}", closure_inferred(1));
    // 一旦闭包的类型被推断出来，就不能再用另一种类型推断了。
    //println!("cannot reuse closure_inferred with another type: {}", closure_inferred(42i64));
    // TODO：取消注释上面一行并查看编译器错误。

    // 一个不接受参数并返回 `i32` 的闭包。
    // 返回类型是推断出来的。
    let one = || 1;
    println!("closure returning one: {}", one());

}
```
