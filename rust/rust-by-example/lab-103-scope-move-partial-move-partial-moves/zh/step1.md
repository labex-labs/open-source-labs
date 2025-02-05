# 部分移动

在单个变量的[解构]过程中，可以同时使用 `按值移动` 和 `按引用` 模式绑定。这样做会导致变量的 _部分移动_，这意味着变量的某些部分会被移动，而其他部分会保留。在这种情况下，父变量之后不能再作为一个整体使用，但是仅被引用（而未被移动）的部分仍然可以使用。

```rust
fn main() {
    #[derive(Debug)]
    struct Person {
        name: String,
        age: Box<u8>,
    }

    let person = Person {
        name: String::from("Alice"),
        age: Box::new(20),
    };

    // `name` 从 `person` 中被移出，但 `age` 被引用
    let Person { name, ref age } = person;

    println!("The person's age is {}", age);

    println!("The person's name is {}", name);

    // 错误！借用了部分移动的值：`person` 发生了部分移动
    //println!("The person struct is {:?}", person);

    // `person` 不能再使用，但 `person.age` 可以使用，因为它没有被移动
    println!("The person's age from person struct is {}", person.age);
}
```

（在这个例子中，我们将 `age` 变量存储在堆上以说明部分移动：如果删除上述代码中的 `ref`，将会出现错误，因为 `person.age` 的所有权会被移动到变量 `age` 上。如果 `Person.age` 存储在栈上，则不需要 `ref`，因为 `age` 的定义会复制 `person.age` 中的数据而不移动它。）
