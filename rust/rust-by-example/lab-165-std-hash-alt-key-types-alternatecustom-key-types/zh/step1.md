# 替代/自定义键类型

任何实现了 `Eq` 和 `Hash` 特性的类型都可以作为 `HashMap` 中的键。这包括：

- `bool`（不过不是很有用，因为只有两个可能的键）
- `int`、`uint` 及其所有变体
- `String` 和 `&str`（提示：你可以有一个以 `String` 为键的 `HashMap`，并使用 `&str` 调用 `.get()`）

注意，`f32` 和 `f64` **没有** 实现 `Hash`，可能是因为浮点精度误差会使将它们用作哈希表键极易出错。

如果所有集合类中包含的类型也分别实现了 `Eq` 和 `Hash`，那么这些集合类也会实现 `Eq` 和 `Hash`。例如，如果 `T` 实现了 `Hash`，那么 `Vec<T>` 也会实现 `Hash`。

你可以通过一行代码轻松地为自定义类型实现 `Eq` 和 `Hash`：`#[derive(PartialEq, Eq, Hash)]`

其余的工作编译器会完成。如果你想对细节有更多控制，可以自己实现 `Eq` 和/或 `Hash`。本指南不会涵盖实现 `Hash` 的具体细节。

为了尝试在 `HashMap` 中使用 `struct`，我们来创建一个非常简单的用户登录系统：

```rust
use std::collections::HashMap;

// Eq 要求你在类型上派生 PartialEq。
#[derive(PartialEq, Eq, Hash)]
struct Account<'a>{
    username: &'a str,
    password: &'a str,
}

struct AccountInfo<'a>{
    name: &'a str,
    email: &'a str,
}

type Accounts<'a> = HashMap<Account<'a>, AccountInfo<'a>>;

fn try_logon<'a>(accounts: &Accounts<'a>,
        username: &'a str, password: &'a str){
    println!("Username: {}", username);
    println!("Password: {}", password);
    println!("Attempting logon...");

    let logon = Account {
        username,
        password,
    };

    match accounts.get(&logon) {
        Some(account_info) => {
            println!("Successful logon!");
            println!("Name: {}", account_info.name);
            println!("Email: {}", account_info.email);
        },
        _ => println!("Login failed!"),
    }
}

fn main(){
    let mut accounts: Accounts = HashMap::new();

    let account = Account {
        username: "j.everyman",
        password: "password123",
    };

    let account_info = AccountInfo {
        name: "John Everyman",
        email: "j.everyman@email.com",
    };

    accounts.insert(account, account_info);

    try_logon(&accounts, "j.everyman", "psasword123");

    try_logon(&accounts, "j.everyman", "password123");
}
```
