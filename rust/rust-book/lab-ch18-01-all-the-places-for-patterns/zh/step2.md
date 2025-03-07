# `match` 分支

如第 6 章所述，我们在 `match` 表达式的分支中使用模式。形式上，`match` 表达式定义为关键字 `match`、要匹配的值，以及一个或多个匹配分支，每个分支由一个模式和一个表达式组成，如果值与该分支的模式匹配，则运行该表达式，如下所示：

```rust
match VALUE {
    PATTERN => EXPRESSION,
    PATTERN => EXPRESSION,
    PATTERN => EXPRESSION,
}
```

例如，下面是清单 6-5 中的 `match` 表达式，它对变量 `x` 中的 `Option<i32>` 值进行匹配：

```rust
match x {
    None => None,
    Some(i) => Some(i + 1),
}
```

此 `match` 表达式中的模式是每个箭头左侧的 `None` 和 `Some(i)`。

`match` 表达式的一个要求是，它们需要是 _详尽无遗的_，也就是说，必须考虑 `match` 表达式中值的所有可能性。确保涵盖每种可能性的一种方法是为最后一个分支使用一个通配模式：例如，一个匹配任何值的变量名永远不会失败，因此涵盖了所有剩余的情况。

特殊模式 `_` 可以匹配任何内容，但它永远不会绑定到变量，因此它通常用于最后一个匹配分支。例如，当你想要忽略任何未指定的值时，`_` 模式可能会很有用。我们将在「忽略模式中的值」中更详细地介绍 `_` 模式。
