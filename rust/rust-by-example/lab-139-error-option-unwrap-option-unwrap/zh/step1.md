# `Option` 与 `unwrap`

在上一个示例中，我们展示了可以随意引发程序失败。我们告诉程序，如果喝到一杯加糖柠檬水就 `panic`。但是，如果我们期望得到 _某种_ 饮品却没有得到呢？这种情况同样糟糕，因此需要进行处理！

我们 _可以_ 像处理柠檬水那样，将其与空字符串（`""`）进行比较。既然我们使用的是 Rust，那就让编译器指出没有饮品的情况吧。

当可能不存在值时，标准库中一个名为 `Option<T>` 的枚举会派上用场。它表现为两种“选项”之一：

- `Some(T)`：找到了类型为 `T` 的一个元素
- `None`：未找到元素

这些情况既可以通过 `match` 进行显式处理，也可以使用 `unwrap` 进行隐式处理。隐式处理要么返回内部元素，要么引发 `panic`。

请注意，可以使用 `expect` 手动自定义 `panic`，但除此之外，`unwrap` 给我们的输出不如显式处理那么有意义。在下面的示例中，显式处理会产生更可控的结果，同时保留了在需要时 `panic` 的选项。

```rust
// 成年人见多识广，能很好地应对任何饮品。
// 所有饮品都使用 `match` 进行显式处理。
fn give_adult(drink: Option<&str>) {
    // 为每种情况指定一个操作流程。
    match drink {
        Some("lemonade") => println!("呸！太甜了。"),
        Some(inner)   => println!("{}？真好喝。", inner),
        None          => println!("没有饮品？好吧。"),
    }
}

// 其他人在喝到加糖饮品之前会 `panic`。
// 所有饮品都使用 `unwrap` 进行隐式处理。
fn drink(drink: Option<&str>) {
    // 当接收到 `None` 时，`unwrap` 会引发 `panic`。
    let inside = drink.unwrap();
    if inside == "lemonade" { panic!("啊啊啊啊啊！！！！"); }

    println!("我超爱 {}！！！！", inside);
}

fn main() {
    let water  = Some("water");
    let lemonade = Some("lemonade");
    let void  = None;

    give_adult(water);
    give_adult(lemonade);
    give_adult(void);

    let coffee = Some("coffee");
    let nothing = None;

    drink(coffee);
    drink(nothing);
}
```
