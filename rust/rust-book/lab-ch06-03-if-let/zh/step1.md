# 使用 `if let` 的简洁控制流

`if let` 语法让你能够将 `if` 和 `let` 组合成一种更简洁的方式，用于处理匹配某一模式的值，同时忽略其他值。考虑清单 6-6 中的程序，它对 `config_max` 变量中的 `Option<u8>` 值进行匹配，但仅在值为 `Some` 变体时才希望执行代码。

```rust
let config_max = Some(3u8);
match config_max {
    Some(max) => println!("The maximum is configured to be {max}"),
    _ => (),
}
```

清单 6-6：一个仅在值为 `Some` 时才关心执行代码的 `match`

如果值为 `Some`，我们通过将值绑定到模式中的变量 `max` 来打印出 `Some` 变体中的值。对于 `None` 值，我们不想执行任何操作。为了满足 `match` 表达式，我们必须在处理完一个变体后添加 `_ => ()`，这是一段烦人的样板代码。

相反，我们可以使用 `if let` 以更短的方式编写此代码。以下代码的行为与清单 6-6 中的 `match` 相同：

```rust
let config_max = Some(3u8);
if let Some(max) = config_max {
    println!("The maximum is configured to be {max}");
}
```

`if let` 语法接受一个由等号分隔的模式和一个表达式。它的工作方式与 `match` 相同，其中表达式被提供给 `match`，而模式是其第一个分支。在这种情况下，模式是 `Some(max)`，并且 `max` 绑定到 `Some` 内部的值。然后，我们可以在 `if let` 块的主体中以与在相应的 `match` 分支中使用 `max` 相同的方式使用 `max`。如果值不匹配模式，则 `if let` 块中的代码不会运行。

使用 `if let` 意味着更少的输入、更少的缩进和更少的样板代码。然而，你失去了 `match` 所强制执行的详尽检查。在 `match` 和 `if let` 之间进行选择取决于你在特定情况下的操作，以及简洁性的提升是否是对失去详尽检查的适当权衡。

换句话说，你可以将 `if let` 视为 `match` 的语法糖，当值匹配一个模式时运行代码，然后忽略所有其他值。

我们可以为 `if let` 包含一个 `else`。与 `else` 相关联的代码块与在与 `if let` 和 `else` 等效的 `match` 表达式中与 `_` 情况相关联的代码块相同。回想一下清单 6-4 中的 `Coin` 枚举定义，其中 `Quarter` 变体还持有一个 `UsState` 值。如果我们想统计我们看到的所有非 25 美分硬币，同时宣布 25 美分硬币的州，我们可以使用 `match` 表达式来实现，如下所示：

```rust
let mut count = 0;
match coin {
    Coin::Quarter(state) => println!("State quarter from {:?}!", state),
    _ => count += 1,
}
```

或者我们可以使用 `if let` 和 `else` 表达式，如下所示：

```rust
let mut count = 0;
if let Coin::Quarter(state) = coin {
    println!("State quarter from {:?}!", state);
} else {
    count += 1;
}
```

如果你遇到一种情况，即你的程序逻辑过于冗长而无法使用 `match` 来表达，请记住 `if let` 也是你 Rust 工具库中的一种选择。
