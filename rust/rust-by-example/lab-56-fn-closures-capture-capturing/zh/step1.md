# 捕获

闭包本质上具有灵活性，会根据功能需求来使闭包正常工作而无需注释。这使得捕获能够灵活地适应不同用例，有时进行移动，有时进行借用。闭包可以按以下方式捕获变量：

- 按引用：`&T`
- 按可变引用：`&mut T`
- 按值：`T`

它们优先按引用捕获变量，只有在必要时才会采用更低级别的方式。

```rust
fn main() {
    use std::mem;

    let color = String::from("green");

    // 一个用于打印 `color` 的闭包，它立即借用（`&`）`color` 并将借用和闭包存储在 `print` 变量中。在最后一次使用 `print` 之前，它将一直保持借用状态。
    //
    // `println!` 仅需要不可变引用作为参数，所以它不会施加更严格的限制。
    let print = || println!("`color`: {}", color);

    // 使用借用调用闭包。
    print();

    // 可以再次不可变地借用 `color`，因为闭包只持有对 `color` 的不可变引用。
    let _reborrow = &color;
    print();

    // 在最后一次使用 `print` 之后，允许进行移动或重新借用
    let _color_moved = color;


    let mut count = 0;
    // 一个用于递增 `count` 的闭包可以采用 `&mut count` 或 `count`，但 `&mut count` 的限制更少，所以它采用了这种方式。立即借用 `count`。
    //
    // `inc` 上需要一个 `mut`，因为内部存储了一个 `&mut`。因此，调用闭包会使闭包发生变异，这就需要一个 `mut`。
    let mut inc = || {
        count += 1;
        println!("`count`: {}", count);
    };

    // 使用可变借用来调用闭包。
    inc();

    // 闭包仍然可变地借用 `count`，因为稍后还会调用它。尝试重新借用会导致错误。
    // let _reborrow = &count;
    // ^ TODO: 尝试取消注释这一行。
    inc();

    // 闭包不再需要借用 `&mut count`。因此，可以进行重新借用而不会出错
    let _count_reborrowed = &mut count;


    // 一个非复制类型。
    let movable = Box::new(3);

    // `mem::drop` 需要 `T`，所以这里必须按值获取。复制类型会复制到闭包中，而原始值保持不变。
    // 非复制类型必须进行移动，所以 `movable` 会立即移动到闭包中。
    let consume = || {
        println!("`movable`: {:?}", movable);
        mem::drop(movable);
    };

    // `consume` 会消耗该变量，所以只能调用一次。
    consume();
    // consume();
    // ^ TODO: 尝试取消注释这一行。
}
```

在垂直管道之前使用 `move` 会强制闭包获取被捕获变量的所有权：

```rust
fn main() {
    // `Vec` 具有非复制语义。
    let haystack = vec![1, 2, 3];

    let contains = move |needle| haystack.contains(needle);

    println!("{}", contains(&1));
    println!("{}", contains(&4));

    // println!("There're {} elements in vec", haystack.len());
    // ^ 取消注释上面这一行会导致编译时错误
    // 因为借用检查器不允许在变量被移动后再次使用它。

    // 从闭包签名中移除 `move` 会导致闭包不可变地借用 `_haystack_` 变量，因此 `_haystack_` 仍然可用，取消注释上面那一行不会导致错误。
}
```
