# 使用结构体进行重构：增加更多含义

我们使用结构体通过为数据添加标签来增加含义。我们可以将正在使用的元组转换为一个结构体，为整个结构体以及各个部分都赋予名称，如清单 5-10 所示。

文件名：`src/main.rs`

```rust
1 struct Rectangle {
  2 width: u32,
    height: u32,
}

fn main() {
  3 let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        area(&rect1)
    );
}

4 fn area(rectangle: &Rectangle) -> u32 {
  5 rectangle.width * rectangle.height
}
```

清单 5-10：定义一个 `Rectangle` 结构体

在这里，我们定义了一个结构体并将其命名为 `Rectangle`\[1\]。在花括号内，我们将字段定义为 `width` 和 `height`，它们的类型都是 `u32`\[2\]。然后，在 `main` 函数中，我们创建了一个 `Rectangle` 的特定实例，其宽度为 `30`，高度为 `50`\[3\]。

我们的 `area` 函数现在定义为带有一个参数，我们将其命名为 `rectangle`，其类型是结构体 `Rectangle` 实例的不可变借用\[4\]。如第 4 章所述，我们希望借用结构体而不是获取其所有权。这样，`main` 函数保留其所有权并可以继续使用 `rect1`，这就是我们在函数签名以及调用函数的地方使用 `&` 的原因。

`area` 函数访问 `Rectangle` 实例的 `width` 和 `height` 字段\[5\]（请注意，访问借用的结构体实例的字段不会移动字段值，这就是为什么你经常会看到对结构体的借用）。我们的 `area` 函数签名现在准确地表达了我们的意图：使用 `Rectangle` 的 `width` 和 `height` 字段来计算其面积。这表明宽度和高度是相互关联的，并且为这些值赋予了描述性名称，而不是使用元组索引值 `0` 和 `1`。这在清晰度方面是一个优势。
