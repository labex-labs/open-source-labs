# 在线编译器

[Rust 在线编译器](https://play.rust-lang.org/) 是一种通过 Web 界面试验 Rust 代码的方式。

## 与 `mdbook` 配合使用

在 `mdbook` 中，你可以使代码示例可运行且可编辑。

```rust
fn main() {
    println!("Hello World!");
}
```

这使读者既能运行你的代码示例，又能对其进行修改和调整。关键在于在代码围栏块中添加单词 `editable`，并用逗号分隔。

````markdown
```rust
//...将你的代码放在这里
```
````

此外，如果你希望 `mdbook` 在构建和测试时跳过你的代码，可以添加 `ignore`。

````markdown
```rust
//...将你的代码放在这里
```
````

## 与文档配合使用

你可能在一些官方 Rust 文档中注意到一个名为 “运行” 的按钮，它会在 Rust 在线编译器的新标签页中打开代码示例。如果你使用名为 `html_playground_url` 的 `#\[doc\]` 属性，此功能将被启用。
