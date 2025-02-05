# 测试用例：链表

实现链表的一种常见方式是通过 `enum`：

```rust
use crate::List::*;

enum List {
    // Cons：元组结构体，封装了一个元素和指向下一个节点的指针
    Cons(u32, Box<List>),
    // Nil：表示链表末尾的节点
    Nil,
}

// 方法可以附加到枚举上
impl List {
    // 创建一个空链表
    fn new() -> List {
        // `Nil` 的类型为 `List`
        Nil
    }

    // 消费一个链表，并返回在其前端添加了新元素的相同链表
    fn prepend(self, elem: u32) -> List {
        // `Cons` 的类型也为 `List`
        Cons(elem, Box::new(self))
    }

    // 返回链表的长度
    fn len(&self) -> u32 {
        // 必须对 `self` 进行匹配，因为此方法的行为
        // 取决于 `self` 的变体
        // `self` 的类型为 `&List`，而 `*self` 的类型为 `List`，在 Rust 2018 之后，
        // 你也可以在这里使用 `self` 并在下面使用 `tail`（不带引用），
        // Rust 会推断出 `&s` 和 `ref tail`。
        // 请参阅 https://doc.rust-lang.org/edition-guide/rust-2018/ownership-and-lifetimes/default-match-bindings.html
        match *self {
            // 不能获取尾部的所有权，因为 `self` 是借用的；
            // 而是获取对尾部的引用
            Cons(_, ref tail) => 1 + tail.len(),
            // 基本情况：空链表的长度为零
            Nil => 0
        }
    }

    // 返回链表作为（堆分配的）字符串的表示形式
    fn stringify(&self) -> String {
        match *self {
            Cons(head, ref tail) => {
                // `format!` 类似于 `print!`，但返回一个堆
                // 分配的字符串而不是打印到控制台
                format!("{}, {}", head, tail.stringify())
            },
            Nil => {
                format!("Nil")
            },
        }
    }
}

fn main() {
    // 创建一个空链表
    let mut list = List::new();

    // 在前端添加一些元素
    list = list.prepend(1);
    list = list.prepend(2);
    list = list.prepend(3);

    // 显示链表的最终状态
    println!("链表的长度为：{}", list.len());
    println!("{}", list.stringify());
}
```
