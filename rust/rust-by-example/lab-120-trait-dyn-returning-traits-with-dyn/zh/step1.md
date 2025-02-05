# 使用 `dyn` 返回 trait

Rust 编译器需要知道每个函数的返回类型需要多少空间。这意味着你所有的函数都必须返回一个具体的类型。与其他语言不同，如果你有一个像 `Animal` 这样的 trait，你不能编写一个返回 `Animal` 的函数，因为它的不同实现需要不同数量的内存。

然而，有一个简单的解决方法。我们的函数不是直接返回一个 trait 对象，而是返回一个包含某个 `Animal` 的 `Box`。一个 `box` 只是对堆中某些内存的引用。因为引用具有静态已知的大小，并且编译器可以保证它指向一个堆分配的 `Animal`，所以我们可以从函数中返回一个 trait！

每当 Rust 在堆上分配内存时，它都会尽可能明确。所以如果你的函数以这种方式返回一个指向堆上 trait 的指针，你需要在返回类型中使用 `dyn` 关键字，例如 `Box<dyn Animal>`。

```rust
struct Sheep {}
struct Cow {}

trait Animal {
    // 实例方法签名
    fn noise(&self) -> &'static str;
}

// 为 `Sheep` 实现 `Animal` trait。
impl Animal for Sheep {
    fn noise(&self) -> &'static str {
        "baaaaah!"
    }
}

// 为 `Cow` 实现 `Animal` trait。
impl Animal for Cow {
    fn noise(&self) -> &'static str {
        "moooooo!"
    }
}

// 返回某个实现了 `Animal` 的结构体，但在编译时我们不知道是哪一个。
fn random_animal(random_number: f64) -> Box<dyn Animal> {
    if random_number < 0.5 {
        Box::new(Sheep {})
    } else {
        Box::new(Cow {})
    }
}

fn main() {
    let random_number = 0.234;
    let animal = random_animal(random_number);
    println!("你随机选择了一种动物，它叫 {}", animal.noise());
}
```
