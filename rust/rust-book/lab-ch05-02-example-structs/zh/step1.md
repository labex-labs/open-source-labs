# 使用结构体的示例程序

为了理解何时可能需要使用结构体，让我们编写一个计算矩形面积的程序。我们将从使用单个变量开始，然后逐步重构程序，直到使用结构体为止。

让我们使用 Cargo 创建一个名为 _rectangles_ 的新二进制项目，该项目将接受以像素为单位指定的矩形的宽度和高度，并计算矩形的面积。清单 5-8 展示了一个简短的程序，这是在我们项目的 `src/main.rs` 中实现此功能的一种方法。

文件名：`src/main.rs`

```rust
fn main() {
    let width1 = 30;
    let height1 = 50;

    println!(
        "The area of the rectangle is {} square pixels.",
        area(width1, height1)
    );
}

fn area(width: u32, height: u32) -> u32 {
    width * height
}
```

清单 5-8：使用单独的宽度和高度变量计算矩形的面积

现在，使用 `cargo run` 运行此程序：

```rust
The area of the rectangle is 1500 square pixels.
```

这段代码通过使用每个维度调用 `area` 函数成功计算出了矩形的面积，但我们可以做更多工作来使这段代码更清晰易读。

这段代码的问题在 `area` 的签名中很明显：

```rust
fn area(width: u32, height: u32) -> u32 {
```

`area` 函数应该计算一个矩形的面积，但我们编写的函数有两个参数，并且在我们的程序中任何地方都不清楚这些参数是相关的。将宽度和高度组合在一起会更具可读性和可管理性。我们已经在“元组类型”中讨论过一种实现方法：使用元组。
