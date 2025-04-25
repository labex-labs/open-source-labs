# 结构体

同样，一个`struct`可以按如下方式解构：

```rust
fn main() {
    struct Foo {
        x: (u32, u32),
        y: u32,
    }

    // 尝试更改结构体中的值，看看会发生什么
    let foo = Foo { x: (1, 2), y: 3 };

    match foo {
        Foo { x: (1, b), y } => println!("First of x is 1, b = {},  y = {} ", b, y),

        // 你可以解构结构体并重命名变量，
        // 顺序并不重要
        Foo { y: 2, x: i } => println!("y is 2, i = {:?}", i),

        // 你也可以忽略一些变量：
        Foo { y,.. } => println!("y = {}, we don't care about x", y),
        // 这会给出一个错误：模式未提及字段 `x`
        //Foo { y } => println!("y = {}", y),
    }

    let faa = Foo { x: (1, 2), y: 3 };

    // 解构结构体不需要 `match` 块：
    let Foo { x : x0, y: y0 } = faa;
    println!("Outside: x0 = {x0:?}, y0 = {y0}");
}
```
