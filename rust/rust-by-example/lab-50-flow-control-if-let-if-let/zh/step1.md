# if let

在某些用例中，当匹配枚举时，`match` 显得很笨拙。例如：

```rust
// 创建一个类型为 `Option<i32>` 的 `optional`
let optional = Some(7);

match optional {
    Some(i) => {
        println!("这是一个很长的字符串，并且 `{:?}`", i);
        // ^ 仅仅为了从选项中解构出 `i`，就需要两个缩进。
    },
    _ => {},
    // ^ 这是必需的，因为 `match` 是穷尽的。这看起来不像是浪费空间吗？
};
```

对于这种用例，`if let` 更简洁，并且还允许指定各种失败选项：

```rust
fn main() {
    // 所有这些变量的类型都是 `Option<i32>`
    let number = Some(7);
    let letter: Option<i32> = None;
    let emoticon: Option<i32> = None;

    // `if let` 结构的含义是：“如果 `let` 将 `number` 解构为 `Some(i)`，则计算代码块 (`{}`)。
    if let Some(i) = number {
        println!("匹配到 {:?}！", i);
    }

    // 如果你需要指定失败情况，使用 `else`：
    if let Some(i) = letter {
        println!("匹配到 {:?}！", i);
    } else {
        // 解构失败。切换到失败情况。
        println!("没有匹配到数字。我们用字母吧！");
    }

    // 提供一个改变后的失败条件。
    let i_like_letters = false;

    if let Some(i) = emoticon {
        println!("匹配到 {:?}！", i);
    // 解构失败。计算一个 `else if` 条件，看是否应该采用备用的失败分支：
    } else if i_like_letters {
        println!("没有匹配到数字。我们用字母吧！");
    } else {
        // 条件计算为 false。这个分支是默认分支：
        println!("我不喜欢字母。我们用表情符号 :) 吧！");
    }
}
```

同样地，`if let` 可用于匹配任何枚举值：

```rust
// 我们的示例枚举
enum Foo {
    Bar,
    Baz,
    Qux(u32)
}

fn main() {
    // 创建示例变量
    let a = Foo::Bar;
    let b = Foo::Baz;
    let c = Foo::Qux(100);

    // 变量 a 匹配 Foo::Bar
    if let Foo::Bar = a {
        println!("a 是 foobar");
    }

    // 变量 b 不匹配 Foo::Bar
    // 所以这不会打印任何内容
    if let Foo::Bar = b {
        println!("b 是 foobar");
    }

    // 变量 c 匹配有值的 Foo::Qux
    // 类似于上一个示例中的 Some()
    if let Foo::Qux(value) = c {
        println!("c 是 {}", value);
    }

    // 绑定在 `if let` 中也有效
    if let Foo::Qux(value @ 100) = c {
        println!("c 是一百");
    }
}
```

另一个好处是，`if let` 允许我们匹配非参数化的枚举变体。即使在枚举没有实现或派生 `PartialEq` 的情况下也是如此。在这种情况下，`if Foo::Bar == a` 会编译失败，因为枚举实例不能进行相等比较，然而 `if let` 仍然可以正常工作。

你想接受一个挑战吗？修复以下示例以使用 `if let`：

```rust
// 这个枚举故意既不实现也不派生 `PartialEq`。
// 这就是为什么下面比较 Foo::Bar == a 会失败。
enum Foo {Bar}

fn main() {
    let a = Foo::Bar;

    // 变量 a 匹配 Foo::Bar
    if Foo::Bar == a {
    // ^-- 这会导致编译时错误。请改用 `if let`。
        println!("a 是 foobar");
    }
}
```
