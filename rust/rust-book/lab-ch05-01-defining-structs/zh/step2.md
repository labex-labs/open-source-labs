# 使用字段初始化简写形式

因为在清单5-4中参数名称和结构体字段名称完全相同，所以我们可以使用*字段初始化简写形式*语法来重写`build_user`函数，使其行为完全相同，但不会重复`username`和`email`，如清单5-5所示。

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username,
        email,
        sign_in_count: 1,
    }
}
```

清单5-5：一个使用字段初始化简写形式的`build_user`函数，因为`username`和`email`参数与结构体字段具有相同的名称

在这里，我们正在创建一个`User`结构体的新实例，它有一个名为`email`的字段。我们想将`email`字段的值设置为`build_user`函数的`email`参数中的值。因为`email`字段和`email`参数具有相同的名称，所以我们只需要写`email`而不是`email: email`。
