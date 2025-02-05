# 在嵌套模式中忽略值的部分

我们还可以在另一个模式中使用 `_` 来仅忽略值的一部分，例如，当我们只想测试值的一部分，而在要运行的相应代码中不需要其他部分时。清单18-18展示了负责管理设置值的代码。业务需求是不允许用户覆盖现有设置的定制，但可以取消设置，如果当前未设置则可以赋予其一个值。

文件名：`src/main.rs`

```rust
let mut setting_value = Some(5);
let new_setting_value = Some(10);

match (setting_value, new_setting_value) {
    (Some(_), Some(_)) => {
        println!("Can't overwrite an existing customized value");
    }
    _ => {
        setting_value = new_setting_value;
    }
}

println!("setting is {:?}", setting_value);
```

清单18-18：在匹配 `Some` 变体的模式中使用下划线，当我们不需要使用 `Some` 内部的值时

这段代码将打印 `Can't overwrite an existing customized value`，然后打印 `setting is Some(5)`。在第一个匹配分支中，我们不需要匹配或使用任一 `Some` 变体内部的值，但我们确实需要测试 `setting_value` 和 `new_setting_value` 都是 `Some` 变体的情况。在这种情况下，我们打印不更改 `setting_value` 的原因，并且它不会被更改。

在第二个分支中由 `_` 模式表示的所有其他情况（即 `setting_value` 或 `new_setting_value` 为 `None`）下，我们希望允许 `new_setting_value` 成为 `setting_value`。

我们还可以在一个模式中的多个位置使用下划线来忽略特定的值。清单18-19展示了一个忽略五元组中第二个和第四个值的示例。

文件名：`src/main.rs`

```rust
let numbers = (2, 4, 8, 16, 32);

match numbers {
    (first, _, third, _, fifth) => {
        println!("Some numbers: {first}, {third}, {fifth}");
    }
}
```

清单18-19：忽略元组的多个部分

这段代码将打印 `Some numbers: 2, 8, 32`，并且值 `4` 和 `16` 将被忽略。
