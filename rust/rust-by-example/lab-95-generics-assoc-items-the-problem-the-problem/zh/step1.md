# 问题

一个在其容器类型上是泛型的 `trait` 有类型规范要求 —— 该 `trait` 的使用者 _必须_ 指定其所有泛型类型。

在下面的示例中，`Contains` `trait` 允许使用泛型类型 `A` 和 `B`。然后为 `Container` 类型实现该 trait，为 `A` 和 `B` 指定 `i32`，以便它可以与 `fn difference()` 一起使用。

因为 `Contains` 是泛型的，所以我们被迫为 `fn difference()` 显式声明所有泛型类型。在实际应用中，我们希望有一种方法来表示 `A` 和 `B` 由输入的 `C` 决定。正如你将在下一节中看到的，关联类型恰好提供了这种能力。

```rust
struct Container(i32, i32);

// 一个用于检查容器中是否存储了两个项的 trait。
// 还可以获取第一个或最后一个值。
trait Contains<A, B> {
    fn contains(&self, _: &A, _: &B) -> bool; // 显式要求 `A` 和 `B`。
    fn first(&self) -> i32; // 不显式要求 `A` 或 `B`。
    fn last(&self) -> i32;  // 不显式要求 `A` 或 `B`。
}

impl Contains<i32, i32> for Container {
    // 如果存储的数字相等，则返回 true。
    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {
        (&self.0 == number_1) && (&self.1 == number_2)
    }

    // 获取第一个数字。
    fn first(&self) -> i32 { self.0 }

    // 获取最后一个数字。
    fn last(&self) -> i32 { self.1 }
}

// `C` 包含 `A` 和 `B`。因此，不得不再次声明 `A` 和
// `B` 很麻烦。
fn difference<A, B, C>(container: &C) -> i32 where
    C: Contains<A, B> {
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
