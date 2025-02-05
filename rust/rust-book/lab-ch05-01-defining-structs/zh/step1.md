# 定义和实例化结构体

结构体与在“元组类型”中讨论的元组类似，它们都可以包含多个相关的值。和元组一样，结构体的各个部分可以是不同的类型。与元组不同的是，在结构体中，你要为每个数据部分命名，这样就能清楚地知道这些值的含义。添加这些名称意味着结构体比元组更灵活：你不必依赖数据的顺序来指定或访问实例的值。

要定义一个结构体，我们输入关键字`struct`并为整个结构体命名。结构体的名称应该描述被组合在一起的数据部分的重要性。然后，在花括号内，我们定义数据部分的名称和类型，我们将这些称为*字段*。例如，清单5-1展示了一个存储用户账户信息的结构体。

文件名：`src/main.rs`

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
```

清单5-1：一个`User`结构体定义

在定义结构体之后要使用它，我们通过为每个字段指定具体的值来创建该结构体的一个*实例*。我们通过声明结构体的名称，然后添加包含键值对的花括号来创建一个实例，其中键是字段的名称，值是我们想要存储在这些字段中的数据。我们不必按照在结构体中声明字段的相同顺序来指定字段。换句话说，结构体定义就像是该类型的一个通用模板，实例用特定的数据填充该模板以创建该类型的值。例如，我们可以像清单5-2那样声明一个特定的用户。

文件名：`src/main.rs`

```rust
fn main() {
    let user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };
}
```

清单5-2：创建一个`User`结构体的实例

要从结构体中获取特定的值，我们使用点号表示法。例如，要访问这个用户的电子邮件地址，我们使用`user1.email`。如果实例是可变的，我们可以通过使用点号表示法并赋值给特定字段来更改值。清单5-3展示了如何更改可变`User`实例的`email`字段中的值。

文件名：`src/main.rs`

```rust
fn main() {
    let mut user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };

    user1.email = String::from("anotheremail@example.com");
}
```

清单5-3：更改`User`实例的`email`字段中的值

请注意，整个实例必须是可变的；Rust不允许我们只将某些字段标记为可变的。与任何表达式一样，我们可以在函数体的最后一个表达式中构造结构体的一个新实例，以隐式返回该新实例。

清单5-4展示了一个`build_user`函数，它返回一个具有给定电子邮件和用户名的`User`实例。`active`字段的值为`true`，`sign_in_count`的值为`1`。

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username: username,
        email: email,
        sign_in_count: 1,
    }
}
```

清单5-4：一个接受电子邮件和用户名并返回`User`实例的`build_user`函数

用与结构体字段相同的名称来命名函数参数是有意义的，但是必须重复`email`和`username`字段名称及变量有点繁琐。如果结构体有更多字段，重复每个名称会更烦人。幸运的是，有一个方便的简写形式！
