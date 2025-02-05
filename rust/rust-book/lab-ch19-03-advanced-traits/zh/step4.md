# 同名方法的歧义消除

Rust 中没有任何规定阻止一个 trait 拥有与另一个 trait 的方法同名的方法，也不阻止你在一个类型上同时实现这两个 trait。直接在类型上实现与 trait 中的方法同名的方法也是可行的。

当调用同名方法时，你需要告诉 Rust 你想要使用哪一个。考虑清单 19-16 中的代码，我们定义了两个 trait，`Pilot` 和 `Wizard`，它们都有一个名为 `fly` 的方法。然后我们在一个已经实现了名为 `fly` 的方法的 `Human` 类型上实现这两个 trait。每个 `fly` 方法的行为都不同。

文件名：`src/main.rs`

```rust
trait Pilot {
    fn fly(&self);
}

trait Wizard {
    fn fly(&self);
}

struct Human;

impl Pilot for Human {
    fn fly(&self) {
        println!("This is your captain speaking.");
    }
}

impl Wizard for Human {
    fn fly(&self) {
        println!("Up!");
    }
}

impl Human {
    fn fly(&self) {
        println!("*waving arms furiously*");
    }
}
```

清单 19-16：定义了两个都有 `fly` 方法的 trait，并在 `Human` 类型上实现它们，同时在 `Human` 上直接实现了一个 `fly` 方法。

当我们在 `Human` 的实例上调用 `fly` 时，编译器默认会调用直接在该类型上实现的方法，如清单 19-17 所示。

文件名：`src/main.rs`

```rust
fn main() {
    let person = Human;
    person.fly();
}
```

清单 19-17：在 `Human` 的实例上调用 `fly`

运行这段代码会打印 `*waving arms furiously*`，这表明 Rust 调用的是直接在 `Human` 上实现的 `fly` 方法。

要调用 `Pilot` trait 或 `Wizard` trait 中的 `fly` 方法，我们需要使用更明确的语法来指定我们想要的是哪个 `fly` 方法。清单 19-18 展示了这种语法。

文件名：`src/main.rs`

```rust
fn main() {
    let person = Human;
    Pilot::fly(&person);
    Wizard::fly(&person);
    person.fly();
}
```

清单 19-18：指定我们想要调用哪个 trait 的 `fly` 方法

在方法名之前指定 trait 名称，向 Rust 明确了我们想要调用哪个 `fly` 实现。我们也可以写成 `Human::fly(&person)`，这与我们在清单 19-18 中使用的 `person.fly()` 等效，但如果我们不需要消除歧义，这样写会更长一些。

运行这段代码会输出以下内容：

    This is your captain speaking.
    Up!
    *waving arms furiously*

因为 `fly` 方法接受一个 `self` 参数，如果我们有两个都实现了同一个 trait 的**类型**，Rust 可以根据 `self` 的类型来确定使用 trait 的哪个实现。

然而，非方法的关联函数没有 `self` 参数。当有多个类型或 trait 定义了具有相同函数名的非方法函数时，除非你使用完全限定语法，否则 Rust 并不总是知道你指的是哪个类型。例如，在清单 19-19 中，我们为一个动物收容所创建了一个 trait，该收容所希望给所有的小狗都取名为 Spot。我们创建了一个 `Animal` trait，它有一个关联的非方法函数 `baby_name`。`Animal` trait 在 `Dog` 结构体上实现，我们也在 `Dog` 上直接提供了一个关联的非方法函数 `baby_name`。

文件名：`src/main.rs`

```rust
trait Animal {
    fn baby_name() -> String;
}

struct Dog;

impl Dog {
    fn baby_name() -> String {
        String::from("Spot")
    }
}

impl Animal for Dog {
    fn baby_name() -> String {
        String::from("puppy")
    }
}

fn main() {
    println!("A baby dog is called a {}", Dog::baby_name());
}
```

清单 19-19：一个带有关联函数的 trait 和一个具有相同名称的关联函数且也实现了该 trait 的类型

我们在 `Dog` 上定义的 `baby_name` 关联函数中实现了给所有小狗取名为 Spot 的代码。`Dog` 类型也实现了 `Animal` trait，该 trait 描述了所有动物共有的特征。小狗被称为 puppy，这在与 `Animal` trait 相关联的 `baby_name` 函数中对 `Dog` 实现 `Animal` trait 时体现出来。

在 `main` 函数中，我们调用 `Dog::baby_name` 函数，它直接调用在 `Dog` 上定义的关联函数。这段代码会输出以下内容：

```rust
A baby dog is called a Spot
```

这不是我们想要的输出。我们想要调用作为 `Animal` trait 一部分且在 `Dog` 上实现的 `baby_name` 函数，这样代码就会打印 `A baby dog is called a puppy`。我们在清单 19-18 中使用的指定 trait 名称的技术在这里不起作用；如果我们将 `main` 函数改为清单 19-20 中的代码，将会得到一个编译错误。

文件名：`src/main.rs`

```rust
fn main() {
    println!("A baby dog is called a {}", Animal::baby_name());
}
```

清单 19-20：尝试调用 `Animal` trait 中的 `baby_name` 函数，但 Rust 不知道使用哪个实现

因为 `Animal::baby_name` 没有 `self` 参数，并且可能有其他类型也实现了 `Animal` trait，所以 Rust 无法确定我们想要的是 `Animal::baby_name` 的哪个实现。我们会得到这个编译器错误：

```bash
error[E0283]: type annotations needed
  --> src/main.rs:20:43
   |
20 |     println!("A baby dog is called a {}", Animal::baby_name());
   |                                           ^^^^^^^^^^^^^^^^^ cannot infer
type
   |
   = note: cannot satisfy `_: Animal`
```

为了消除歧义并告诉 Rust 我们想要使用 `Dog` 对 `Animal` 的实现，而不是其他类型对 `Animal` 的实现，我们需要使用完全限定语法。清单 19-21 展示了如何使用完全限定语法。

文件名：`src/main.rs`

```rust
fn main() {
    println!(
        "A baby dog is called a {}",
        <Dog as Animal>::baby_name()
    );
}
```

清单 19-21：使用完全限定语法指定我们想要调用 `Dog` 上实现的 `Animal` trait 中的 `baby_name` 函数

我们在尖括号内为 Rust 提供了一个类型注释，这表明我们希望通过将 `Dog` 类型视为 `Animal` 来调用 `Dog` 上实现的 `Animal` trait 中的 `baby_name` 方法。现在这段代码会打印出我们想要的内容：

```rust
A baby dog is called a puppy
```

一般来说，完全限定语法定义如下：

```rust
<Type as Trait>::function(receiver_if_method, next_arg,...);
```

对于不是方法的关联函数，不会有 `receiver`：只会有其他参数列表。你可以在调用函数或方法的任何地方使用完全限定语法。然而，如果 Rust 可以从程序中的其他信息推断出，你可以省略此语法的任何部分。只有在有多个使用相同名称的实现且 Rust 需要帮助来确定你想要调用哪个实现的情况下，才需要使用这种更冗长的语法。
