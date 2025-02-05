# 关联类型

“关联类型”的使用通过将内部类型作为 _输出_ 类型局部地移入 trait 中，提高了代码的整体可读性。`trait` 定义的语法如下：

```rust
// `A` 和 `B` 通过 `type` 关键字在 trait 中定义。
// （注意：这里的 `type` 与用于别名时的 `type` 不同）。
trait Contains {
    type A;
    type B;

    // 更新后的语法，用于泛型地引用这些新类型。
    fn contains(&self, _: &Self::A, _: &Self::B) -> bool;
}
```

请注意，使用 `Contains` trait 的函数不再需要显式地表达 `A` 或 `B`：

```rust
// 不使用关联类型
fn difference<A, B, C>(container: &C) -> i32 where
    C: Contains<A, B> {... }

// 使用关联类型
fn difference<C: Contains>(container: &C) -> i32 {... }
```

让我们使用关联类型重写上一节中的示例：

```rust
struct Container(i32, i32);

// 一个 trait，用于检查容器中是否存储了两个项。
// 还可以获取第一个或最后一个值。
trait Contains {
    // 在这里定义泛型类型，方法可以使用这些类型。
    type A;
    type B;

    fn contains(&self, _: &Self::A, _: &Self::B) -> bool;
    fn first(&self) -> i32;
    fn last(&self) -> i32;
}

impl Contains for Container {
    // 指定 `A` 和 `B` 是什么类型。如果 `input` 类型是 `Container(i32, i32)`，则 `output` 类型确定为 `i32` 和 `i32`。
    type A = i32;
    type B = i32;

    // `&Self::A` 和 `&Self::B` 在这里也是有效的。
    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {
        (&self.0 == number_1) && (&self.1 == number_2)
    }
    // 获取第一个数字。
    fn first(&self) -> i32 { self.0 }

    // 获取最后一个数字。
    fn last(&self) -> i32 { self.1 }
}

fn difference<C: Contains>(container: &C) -> i32 {
    container.last() - container.first()
}

fn main() {
    let number_1 = 3;
    let number_2 = 10;

    let container = Container(number_1, number_2);

    println!("容器中是否包含 {} 和 {}: {}",
        &number_1, &number_2,
        container.contains(&number_1, &number_2));
    println!("第一个数字: {}", container.first());
    println!("最后一个数字: {}", container.last());

    println!("差值是: {}", difference(&container));
}
```
