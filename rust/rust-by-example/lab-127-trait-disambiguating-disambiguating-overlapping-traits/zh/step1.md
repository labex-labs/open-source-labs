# 消除重叠特征的歧义

一个类型可以实现许多不同的特征。如果两个特征都需要相同的名称会怎样？例如，许多特征可能都有一个名为 `get()` 的方法。它们甚至可能有不同的返回类型！

好消息是：因为每个特征实现都有自己的 `impl` 块，所以很清楚你正在实现哪个特征的 `get` 方法。

那么当需要调用这些方法时会怎样呢？为了消除它们之间的歧义，我们必须使用完全限定语法。

```rust
trait UsernameWidget {
    // 从这个小部件中获取所选的用户名
    fn get(&self) -> String;
}

trait AgeWidget {
    // 从这个小部件中获取所选的年龄
    fn get(&self) -> u8;
}

// 一个同时具有 UsernameWidget 和 AgeWidget 的表单
struct Form {
    username: String,
    age: u8,
}

impl UsernameWidget for Form {
    fn get(&self) -> String {
        self.username.clone()
    }
}

impl AgeWidget for Form {
    fn get(&self) -> u8 {
        self.age
    }
}

fn main() {
    let form = Form {
        username: "rustacean".to_owned(),
        age: 28,
    };

    // 如果你取消注释这一行，你会得到一个错误，提示
    // “找到多个 `get`”。毕竟，有多个名为 `get` 的方法。
    // println!("{}", form.get());

    let username = <Form as UsernameWidget>::get(&form);
    assert_eq!("rustacean".to_owned(), username);
    let age = <Form as AgeWidget>::get(&form);
    assert_eq!(28, age);
}
```
