# 结构体定义中的生命周期标注

到目前为止，我们定义的结构体都持有拥有所有权的类型。我们可以定义结构体来持有引用，但在这种情况下，我们需要在结构体定义中的每个引用上添加生命周期标注。清单 10-24 中有一个名为 `ImportantExcerpt` 的结构体，它持有一个字符串切片。

文件名：`src/main.rs`

```rust
1 struct ImportantExcerpt<'a> {
  2 part: &'a str,
}

fn main() {
  3 let novel = String::from(
        "Call me Ishmael. Some years ago..."
    );
  4 let first_sentence = novel
       .split('.')
       .next()
       .expect("Could not find a '.'");
  5 let i = ImportantExcerpt {
        part: first_sentence,
    };
}
```

清单 10-24：一个持有引用的结构体，需要生命周期标注

这个结构体有一个名为 `part` 的字段，它持有一个字符串切片，这是一个引用（第 2 行）。与泛型数据类型一样，我们在结构体名称后的尖括号内声明泛型生命周期参数的名称，以便我们可以在结构体定义的主体中使用生命周期参数（第 1 行）。这个标注意味着 `ImportantExcerpt` 的实例不能比它在 `part` 字段中持有的引用存活时间更长。

这里的 `main` 函数创建了一个 `ImportantExcerpt` 结构体的实例（第 5 行），该实例持有对变量 `novel`（第 3 行）所拥有的 `String` 的第一句话的引用（第 4 行）。`novel` 中的数据在 `ImportantExcerpt` 实例创建之前就已存在。此外，在 `ImportantExcerpt` 超出作用域之前，`novel` 不会超出作用域，因此 `ImportantExcerpt` 实例中的引用是有效的。
