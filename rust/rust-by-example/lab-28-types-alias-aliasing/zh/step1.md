# 别名

`type` 语句可用于为现有类型赋予新名称。类型必须使用 `UpperCamelCase` 命名，否则编译器会发出警告。此规则的例外是原始类型：`usize`、`f32` 等。

```rust
// `NanoSecond`、`Inch` 和 `U64` 是 `u64` 的新名称。
type NanoSecond = u64;
type Inch = u64;
type U64 = u64;

fn main() {
    // `NanoSecond` = `Inch` = `U64` = `u64`。
    let nanoseconds: NanoSecond = 5 as U64;
    let inches: Inch = 2 as U64;

    // 请注意，类型别名 *不会* 提供任何额外的类型安全性，因为
    // 别名 *不是* 新类型
    println!("{} 纳秒 + {} 英寸 = {} 个单位？",
             nanoseconds,
             inches,
             nanoseconds + inches);
}
```

别名的主要用途是减少样板代码；例如，`io::Result<T>` 类型是 `Result<T, io::Error>` 类型的别名。
