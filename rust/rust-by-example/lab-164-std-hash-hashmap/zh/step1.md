# HashMap

向量通过整数索引来存储值，而`HashMap`则通过键来存储值。`HashMap`的键可以是布尔值、整数、字符串，或者任何其他实现了`Eq`和`Hash`特征的类型。下一节会详细介绍。

与向量一样，`HashMap`是可增长的，但当有多余空间时，`HashMap`也可以自行收缩。你可以使用`HashMap::with_capacity(uint)`创建具有特定初始容量的`HashMap`，或者使用`HashMap::new()`来获取具有默认初始容量的`HashMap`（推荐）。

```rust
use std::collections::HashMap;

fn call(number: &str) -> &str {
    match number {
        "798-1364" => "We're sorry, the call cannot be completed as dialed.
            Please hang up and try again.",
        "645-7689" => "Hello, this is Mr. Awesome's Pizza. My name is Fred.
            What can I get for you today?",
        _ => "Hi! Who is this again?"
    }
}

fn main() {
    let mut contacts = HashMap::new();

    contacts.insert("Daniel", "798-1364");
    contacts.insert("Ashley", "645-7689");
    contacts.insert("Katie", "435-8291");
    contacts.insert("Robert", "956-1745");

    // 接受一个引用并返回 Option<&V>
    match contacts.get(&"Daniel") {
        Some(&number) => println!("Calling Daniel: {}", call(number)),
        _ => println!("Don't have Daniel's number."),
    }

    // `HashMap::insert()` 如果插入的值是新的，则返回 `None`，否则返回 `Some(value)`
    contacts.insert("Daniel", "164-6743");

    match contacts.get(&"Ashley") {
        Some(&number) => println!("Calling Ashley: {}", call(number)),
        _ => println!("Don't have Ashley's number."),
    }

    contacts.remove(&"Ashley");

    // `HashMap::iter()` 返回一个迭代器，它以任意顺序生成
    // (&'a key, &'a value) 对。
    for (contact, &number) in contacts.iter() {
        println!("Calling {}: {}", contact, call(number));
    }
}
```

有关哈希和哈希映射（有时称为哈希表）的工作原理的更多信息，请查看维基百科上的哈希表词条。
