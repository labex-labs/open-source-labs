# @ 绑定

at 运算符 `@` 让我们在测试值是否匹配某个模式的同时，创建一个持有该值的变量。在清单18-29中，我们想要测试 `Message::Hello` 的 `id` 字段是否在 `3..=7` 范围内。我们还想将该值绑定到变量 `id_variable`，以便在与该分支关联的代码中使用它。我们可以将这个变量命名为 `id`，与字段名相同，但在这个示例中我们将使用不同的名称。

文件名：`src/main.rs`

```rust
enum Message {
    Hello { id: i32 },
}

let msg = Message::Hello { id: 5 };

match msg {
    Message::Hello {
        id: id_variable @ 3..=7,
    } => println!("Found an id in range: {id_variable}"),
    Message::Hello { id: 10..=12 } => {
        println!("Found an id in another range")
    }
    Message::Hello { id } => println!("Some other id: {id}"),
}
```

清单18-29：使用 `@` 在模式中绑定值的同时进行测试

这个示例将打印 `Found an id in range: 5`。通过在范围 `3..=7` 之前指定 `id_variable @`，我们捕获了与该范围匹配的任何值，同时也测试了该值是否匹配范围模式。

在第二个分支中，我们在模式中只指定了一个范围，与该分支关联的代码没有一个包含 `id` 字段实际值的变量。`id` 字段的值可能是10、11或12，但与该模式相关的代码并不知道是哪一个。模式代码无法使用 `id` 字段的值，因为我们没有将 `id` 值保存在变量中。

在最后一个分支中，我们指定了一个没有范围的变量，我们确实有一个名为 `id` 的变量，其值可在该分支的代码中使用。原因是我们使用了结构体字段简写语法。但在这个分支中，我们没有像前两个分支那样对 `id` 字段的值进行任何测试：任何值都将匹配这个模式。

使用 `@` 让我们能够在一个模式中测试一个值并将其保存在一个变量中。
