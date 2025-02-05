# 结构体可见性

结构体的字段具有额外的可见性级别。其可见性默认为私有，可使用 `pub` 修饰符进行覆盖。此可见性仅在从定义结构体的模块外部访问结构体时才重要，其目的是隐藏信息（封装）。

```rust
mod my {
    // 一个具有泛型类型 `T` 的公共字段的公共结构体
    pub struct OpenBox<T> {
        pub contents: T,
    }

    // 一个具有泛型类型 `T` 的私有字段的公共结构体
    pub struct ClosedBox<T> {
        contents: T,
    }

    impl<T> ClosedBox<T> {
        // 一个公共构造函数方法
        pub fn new(contents: T) -> ClosedBox<T> {
            ClosedBox {
                contents: contents,
            }
        }
    }
}

fn main() {
    // 具有公共字段的公共结构体可以像往常一样构造
    let open_box = my::OpenBox { contents: "public information" };

    // 并且它们的字段可以正常访问。
    println!("The open box contains: {}", open_box.contents);

    // 具有私有字段的公共结构体不能使用字段名来构造。
    // 错误！`ClosedBox` 有私有字段
    //let closed_box = my::ClosedBox { contents: "classified information" };
    // TODO ^ 尝试取消注释这一行

    // 然而，具有私有字段的结构体可以使用
    // 公共构造函数来创建
    let _closed_box = my::ClosedBox::new("classified information");

    // 并且公共结构体的私有字段不能被访问。
    // 错误！`contents` 字段是私有的
    //println!("The closed box contains: {}", _closed_box.contents);
    // TODO ^ 尝试取消注释这一行
}
```
