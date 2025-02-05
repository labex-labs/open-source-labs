# 为共同行为定义一个 trait

为了实现我们期望 `gui` 具备的行为，我们将定义一个名为 `Draw` 的 trait，它将有一个名为 `draw` 的方法。然后我们可以定义一个包含 trait 对象的向量。trait 对象指向实现我们指定 trait 的类型的实例以及一个用于在运行时查找该类型上 trait 方法的表。我们通过指定某种指针（例如 `&` 引用或 `Box<T>` 智能指针），然后是 `dyn` 关键字，再指定相关 trait 来创建一个 trait 对象。（我们将在“动态大小类型和 Sized trait”中讨论 trait 对象必须使用指针的原因。）我们可以使用 trait 对象来代替泛型或具体类型。无论我们在哪里使用 trait 对象，Rust 的类型系统都会在编译时确保在该上下文中使用的任何值都将实现 trait 对象的 trait。因此，我们不需要在编译时知道所有可能的类型。

我们已经提到过，在 Rust 中，我们避免将结构体和枚举称为“对象”，以将它们与其他语言中的对象区分开来。在结构体或枚举中，结构体字段中的数据和 `impl` 块中的行为是分开的，而在其他语言中，数据和行为组合成一个概念通常被称为对象。然而，trait 对象在某种意义上更类似于其他语言中的对象，因为它们将数据和行为组合在一起。但 trait 对象与传统对象的不同之处在于，我们不能向 trait 对象添加数据。trait 对象不像其他语言中的对象那样普遍有用：它们的特定目的是允许对共同行为进行抽象。

清单 17-3 展示了如何定义一个名为 `Draw` 的 trait，它有一个名为 `draw` 的方法。

文件名：`src/lib.rs`

```rust
pub trait Draw {
    fn draw(&self);
}
```

清单 17-3：`Draw` trait 的定义

从我们在第 10 章关于如何定义 trait 的讨论中，这种语法应该看起来很熟悉。接下来是一些新语法：清单 17-4 定义了一个名为 `Screen` 的结构体，它包含一个名为 `components` 的向量。这个向量的类型是 `Box<dyn Draw>`，这是一个 trait 对象；它是 `Box` 内部任何实现 `Draw` trait 的类型的替身。

文件名：`src/lib.rs`

```rust
pub struct Screen {
    pub components: Vec<Box<dyn Draw>>,
}
```

清单 17-4：`Screen` 结构体的定义，其 `components` 字段包含一个实现 `Draw` trait 的 trait 对象向量

在 `Screen` 结构体上，我们将定义一个名为 `run` 的方法，它将对其每个 `components` 调用 `draw` 方法，如清单 17-5 所示。

文件名：`src/lib.rs`

```rust
impl Screen {
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

清单 17-5：`Screen` 上的 `run` 方法，它对每个组件调用 `draw` 方法

这与定义一个使用带有 trait 边界的泛型类型参数的结构体的工作方式不同。泛型类型参数一次只能用一个具体类型替换，而 trait 对象允许在运行时有多个具体类型来填充 trait 对象。例如，我们可以使用泛型和 trait 边界来定义 `Screen` 结构体，如清单 17-6 所示。

文件名：`src/lib.rs`

```rust
pub struct Screen<T: Draw> {
    pub components: Vec<T>,
}

impl<T> Screen<T>
where
    T: Draw,
{
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

清单 17-6：使用泛型和 trait 边界的 `Screen` 结构体及其 `run` 方法的另一种实现

这将我们限制为一个 `Screen` 实例，它具有一个全是 `Button` 类型或全是 `TextField` 类型的组件列表。如果你只需要同质集合，使用泛型和 trait 边界会更好，因为定义将在编译时进行单态化以使用具体类型。

另一方面，使用 trait 对象的方法，一个 `Screen` 实例可以持有一个 `Vec<T>`，其中包含一个 `Box<Button>` 以及一个 `Box<TextField>`。让我们看看这是如何工作的，然后我们将讨论其运行时性能影响。
