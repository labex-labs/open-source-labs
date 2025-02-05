# 使用..=匹配值的范围

`..=` 语法允许我们匹配一个包含边界值的范围。在以下代码中，当一个模式与给定范围内的任何值匹配时，该分支将执行：

文件名：`src/main.rs`

```rust
let x = 5;

match x {
    1..=5 => println!("one through five"),
    _ => println!("something else"),
}
```

如果 `x` 是 `1`、`2`、`3`、`4` 或 `5`，第一个分支将匹配。与使用 `|` 运算符来表达相同的想法相比，这种语法对于多个匹配值来说更方便；如果我们使用 `|`，我们必须指定 `1 | 2 | 3 | 4 | 5`。指定一个范围要短得多，特别是如果我们想要匹配比如说1到1000之间的任何数字！

编译器在编译时会检查范围是否为空，并且因为Rust能够判断范围是否为空的唯一类型是 `char` 和数值类型，所以范围只允许用于数值或 `char` 值。

这里有一个使用 `char` 值范围的示例：

文件名：`src/main.rs`

```rust
let x = 'c';

match x {
    'a'..='j' => println!("early ASCII letter"),
    'k'..='z' => println!("late ASCII letter"),
    _ => println!("something else"),
}
```

Rust能够判断出 `'c'` 在第一个模式的范围内，并打印出 `early ASCII letter`。
