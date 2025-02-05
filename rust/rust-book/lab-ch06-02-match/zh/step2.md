# 绑定到值的模式

`match` 分支的另一个有用特性是它们可以绑定到与模式匹配的值的各个部分。这就是我们从枚举变体中提取值的方式。

例如，让我们将枚举变体之一改为在其中包含数据。从 1999 年到 2008 年，美国铸造了 25 美分硬币，其一面为 50 个州中的每个州设计了不同图案。没有其他硬币有州图案，所以只有 25 美分硬币有这个额外的值。我们可以通过将 `Quarter` 变体改为包含存储在其中的 `UsState` 值，将此信息添加到我们的 `enum` 中，我们已经在清单 6-4 中这样做了。

```rust
#[derive(Debug)] // 这样我们稍后就能检查状态
enum UsState {
    Alabama,
    Alaska,
    --省略部分--
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}
```

清单 6-4：一个 `Coin` 枚举，其中 `Quarter` 变体还包含一个 `UsState` 值

假设你的一个朋友正在尝试收集所有 50 个州的 25 美分硬币。当我们按硬币类型整理零钱时，我们还会说出与每个 25 美分硬币相关的州名，这样如果是朋友没有的州，他们就可以将其添加到收藏中。

在这段代码的 `match` 表达式中，我们在与变体 `Coin::Quarter` 的值匹配的模式中添加了一个名为 `state` 的变量。当 `Coin::Quarter` 匹配时，`state` 变量将绑定到该 25 美分硬币的州的值。然后我们可以在该分支的代码中使用 `state`，如下所示：

```rust
fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            25
        }
    }
}
```

如果我们调用 `value_in_cents(Coin::Quarter(UsState::Alaska))`，`coin` 将是 `Coin::Quarter(UsState::Alaska)`。当我们将该值与每个 `match` 分支进行比较时，在到达 `Coin::Quarter(state)` 之前，它们都不匹配。在这一点上，`state` 的绑定将是值 `UsState::Alaska`。然后我们可以在 `println!` 表达式中使用该绑定，从而从 `Coin` 枚举变体 `Quarter` 中获取内部的州值。
