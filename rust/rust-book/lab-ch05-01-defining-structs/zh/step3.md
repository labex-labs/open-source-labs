# 使用结构体更新语法从其他实例创建实例

创建一个结构体的新实例，其中包含另一个实例的大部分值，但有一些更改，这通常很有用。你可以使用*结构体更新语法*来做到这一点。

首先，在清单 5-6 中，我们展示了如何在没有更新语法的情况下常规地在`user2`中创建一个新的`User`实例。我们为`email`设置了一个新值，但其他方面使用我们在清单 5-2 中创建的`user1`中的相同值。

文件名：`src/main.rs`

```rust
fn main() {
    --snip--

    let user2 = User {
        active: user1.active,
        username: user1.username,
        email: String::from("another@example.com"),
        sign_in_count: user1.sign_in_count,
    };
}
```

清单 5-6：使用`user1`中的一个值创建一个新的`User`实例

使用结构体更新语法，我们可以用更少的代码实现相同的效果，如清单 5-7 所示。语法`..`指定未明确设置的其余字段应具有与给定实例中的字段相同的值。

文件名：`src/main.rs`

```rust
fn main() {
    --snip--


    let user2 = User {
        email: String::from("another@example.com"),
      ..user1
    };
}
```

清单 5-7：使用结构体更新语法为`User`实例设置新的`email`值，但使用`user1`中的其余值

清单 5-7 中的代码也在`user2`中创建了一个实例，该实例的`email`值不同，但`username`、`active`和`sign_in_count`字段的值与`user1`中的相同。`..user1`必须放在最后，以指定任何其余字段应从`user1`中的相应字段获取其值，但我们可以选择以任何顺序为任意数量的字段指定值，而不管结构体定义中字段的顺序如何。

请注意，结构体更新语法使用`=`就像赋值一样；这是因为它移动了数据，就像我们在“变量和数据与移动的交互”中看到的那样。在这个例子中，创建`user2`之后我们就不能再使用`user1`了，因为`user1`的`username`字段中的`String`被移动到了`user2`中。如果我们为`user2`的`email`和`username`都赋予了新的`String`值，因此只使用了`user1`中的`active`和`sign_in_count`值，那么在创建`user2`之后`user1`仍然是有效的。`active`和`sign_in_count`都是实现了`Copy` trait 的类型，所以我们在“仅栈数据：Copy”中讨论的行为将会适用。
