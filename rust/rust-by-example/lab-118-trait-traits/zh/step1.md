# 特性（Trait）

“特性（trait）”是为未知类型 `Self` 定义的一组方法。它们可以访问在同一特性中声明的其他方法。

特性可以为任何数据类型实现。在下面的示例中，我们定义了 `Animal`，这是一组方法。然后为 `Sheep` 数据类型实现了 `Animal` 特性，从而允许对 `Sheep` 使用来自 `Animal` 的方法。

```rust
struct Sheep { naked: bool, name: &'static str }

trait Animal {
    // 关联函数签名；`Self` 指代实现类型。
    fn new(name: &'static str) -> Self;

    // 方法签名；这些将返回一个字符串。
    fn name(&self) -> &'static str;
    fn noise(&self) -> &'static str;

    // 特性可以提供默认方法定义。
    fn talk(&self) {
        println!("{} says {}", self.name(), self.noise());
    }
}

impl Sheep {
    fn is_naked(&self) -> bool {
        self.naked
    }

    fn shear(&mut self) {
        if self.is_naked() {
            // 实现者方法可以使用实现者的特性方法。
            println!("{} is already naked...", self.name());
        } else {
            println!("{} gets a haircut!", self.name);

            self.naked = true;
        }
    }
}

// 为 `Sheep` 实现 `Animal` 特性。
impl Animal for Sheep {
    // `Self` 是实现类型：`Sheep`。
    fn new(name: &'static str) -> Sheep {
        Sheep { name: name, naked: false }
    }

    fn name(&self) -> &'static str {
        self.name
    }

    fn noise(&self) -> &'static str {
        if self.is_naked() {
            "baaaaah?"
        } else {
            "baaaaah!"
        }
    }

    // 默认特性方法可以被重写。
    fn talk(&self) {
        // 例如，我们可以添加一些安静的沉思。
        println!("{} pauses briefly... {}", self.name, self.noise());
    }
}

fn main() {
    // 在这种情况下类型注释是必要的。
    let mut dolly: Sheep = Animal::new("Dolly");
    // TODO ^ 尝试移除类型注释。

    dolly.talk();
    dolly.shear();
    dolly.talk();
}
```
